import pytest
import json
import requests


class TestUserAgent:
    user_agents = {
        "user_agent_1": "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 "
                        "(KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "user_agent_2": "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                        "CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
        "user_agent_3": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "user_agent_4": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
        "user_agent_5": "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 "
                        "(KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    }

    expected_values = {
        "expected_values_1": {"platform": "Mobile", "browser": "No", "device": "Android"},
        "expected_values_2": {"platform": "Mobile", "browser": "Chrome", "device": "iOS"},
        "expected_values_3": {"platform": "Googlebot", "browser": "Unknown", "device": "Unknown"},
        "expected_values_4": {"platform": "Web", "browser": "Chrome", "device": "No"},
        "expected_values_5": {"platform": "Mobile", "browser": "No", "device": "iPhone"}
    }
    expected_results = [
        (user_agents["user_agent_1"],
         expected_values["expected_values_1"]["platform"],
         expected_values["expected_values_1"]["browser"],
         expected_values["expected_values_1"]["device"]),
        (user_agents["user_agent_2"],
         expected_values["expected_values_2"]["platform"],
         expected_values["expected_values_2"]["browser"],
         expected_values["expected_values_2"]["device"]),
        (user_agents["user_agent_3"],
         expected_values["expected_values_3"]["platform"],
         expected_values["expected_values_3"]["browser"],
         expected_values["expected_values_3"]["device"]),
        (user_agents["user_agent_4"],
         expected_values["expected_values_4"]["platform"],
         expected_values["expected_values_4"]["browser"],
         expected_values["expected_values_4"]["device"]),
        (user_agents["user_agent_5"],
         expected_values["expected_values_5"]["platform"],
         expected_values["expected_values_5"]["browser"],
         expected_values["expected_values_5"]["device"])
    ]

    @pytest.mark.parametrize('user_agent,platform,browser,device', expected_results)
    def test_check(self, user_agent, platform, browser, device):
        test_url = 'https://playground.learnqa.ru/ajax/api/user_agent_check'
        resp = requests.get(test_url, headers={"User-Agent": user_agent})
        assert resp.json()["platform"] == platform, f"'platform' is wrong. Thruth: {platform}"
        assert resp.json()["browser"] == browser, f"'browser' is wrong. Thruth: {browser}"
        assert resp.json()["device"] == device, f"'device' is wrong. Thruth: {device}"