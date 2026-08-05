// business_reader.zig
// Advisory Locking PostgreSQL pour production concurrente de partitions .piano-diff
// IntentHash: 0xBUSINESS_READER_20260803
// Architecture: N423 / L4-TOOLS
// Pattern: Odoo pg_advisory_lock -> gerivdb advisory locking

const std = @import("std");
const postgres = @import("postgres");

pub const AdvisoryLock = struct {
    conn: *postgres.Connection,
    lock_id: u64,
    acquired: bool,

    pub fn init(conn: *postgres.Connection, lock_id: u64) !AdvisoryLock {
        var lock = AdvisoryLock{
            .conn = conn,
            .lock_id = lock_id,
            .acquired = false,
        };

        // Tentative d'acquisition non-bloquante (pg_try_advisory_lock)
        try lock.acquire();
        return lock;
    }

    pub fn acquire(self: *AdvisoryLock) !void {
        const query = "SELECT pg_try_advisory_lock($1)";
        var result = try self.conn.execQuery(query, .{self.lock_id});
        if (result.rows.len == 0) {
            return error.LockAcquisitionFailed;
        }

        const acquired = result.rows[0].columns[0].bool;
        if (!acquired) {
            return error.LockAcquisitionFailed;
        }

        self.acquired = true;
    }

    pub fn release(self: *AdvisoryLock) !void {
        if (!self.acquired) return;

        const query = "SELECT pg_advisory_unlock($1)";
        _ = try self.conn.execQuery(query, .{self.lock_id});
        self.acquired = false;
    }

    pub fn deinit(self: *AdvisoryLock) void {
        // Cleanup automatique en cas de panic
        if (self.acquired) {
            // Best effort unlock
            const query = "SELECT pg_advisory_unlock($1)";
            self.conn.execQuery(query, .{self.lock_id}) catch {};
            self.acquired = false;
        }
    }
};

pub fn generatePianoDiffPartition(
    conn: *postgres.Connection,
    partition_id: u64,
    knowledge_fragment: []const u8,
) !void {
    // Verrouillage par partition pour éviter les conflits
    var lock = try AdvisoryLock.init(conn, partition_id);
    defer lock.deinit() catch {};

    // Génération du fragment .piano-diff
    const query =
        \\INSERT INTO piano_diff_partitions (partition_id, fragment, created_at)
        \\VALUES ($1, $2, NOW())
        \\ON CONFLICT (partition_id) DO UPDATE SET
        \\  fragment = EXCLUDED.fragment,
        \\  updated_at = NOW()
    ;

    _ = try conn.execQuery(query, .{ partition_id, knowledge_fragment });
}

pub fn readPianoDiffPartition(
    conn: *postgres.Connection,
    partition_id: u64,
) ![]const u8 {
    // Lecture sans verrouillage exclusif
    const query = "SELECT fragment FROM piano_diff_partitions WHERE partition_id = $1";
    var result = try conn.execQuery(query, .{partition_id});

    if (result.rows.len == 0) {
        return error.PartitionNotFound;
    }

    return result.rows[0].columns[0].text;
}
