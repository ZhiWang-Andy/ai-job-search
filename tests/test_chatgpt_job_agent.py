import json

import chatgpt_job_agent as agent


def test_slugify():
    assert agent.slugify("Goldman Sachs / Quant Research (PhD)") == "goldman-sachs-quant-research-phd"


def test_profile_files_exist():
    assert agent.PROFILE_PATH.exists()
    assert agent.MASTER_CV_PATH.exists()
    assert agent.PREFERENCES_PATH.exists()


def test_search_preferences_are_personalized():
    data = json.loads(agent.PREFERENCES_PATH.read_text(encoding="utf-8"))
    assert data["candidate"] == "Zhi Wang"
    assert "Quantitative Research Intern (PhD)" in data["primary_roles"]
    assert data["graduation"] == "May 2028"
