#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du router_utils.py
"""

from agents.router_utils import RouterUtils


class TestRouterUtils:
    def test_route_match(self):
        routes = {"double": lambda x: x * 2}
        router = RouterUtils(routes)
        result = router.route("double", 3)
        assert result.handled is True
        assert result.result == 6

    def test_route_missing(self):
        router = RouterUtils({})
        result = router.route("missing", 1)
        assert result.handled is False
        assert result.error == "no route"

    def test_route_error(self):
        def bad(x):
            raise RuntimeError("boom")

        router = RouterUtils({"bad": bad})
        result = router.route("bad", 1)
        assert result.handled is True
        assert result.error == "boom"
