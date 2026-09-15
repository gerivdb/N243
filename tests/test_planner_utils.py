#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du planner_utils.py
"""

from agents.planner_utils import PlannerUtils


class TestPlannerUtils:
    def test_add_step_and_plan(self):
        planner = PlannerUtils()
        planner.add_step("step1")
        planner.add_step("step2")
        assert planner.plan() == ["step1", "step2"]

    def test_report(self):
        planner = PlannerUtils()
        planner.add_step("step1")
        result = planner.report()
        assert result.steps == 1
        assert result.plan == ["step1"]
