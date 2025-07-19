"""Test routes"""

import json
from unittest.mock import MagicMock, patch

import pytest
from starlette.testclient import TestClient


class TestHealthcheckRoute:
    """Test healthcheck responses."""

    def test_get_health(self, client):
        """Tests a good response"""
        response = client.get("/healthcheck")
        assert 200 == response.status_code
        assert "OK" == response.json()["status"]


class TestBergamoRoute:
    """Test responses."""

    @patch("aind_session_json_service_server.route.BergamoEtl.run_job")
    def test_get_200_response(
        self, mock_run_etl_job: MagicMock, client: TestClient
    ):
        """Tests a good response"""

        post_request_content = {
            "input_source": "abc/def",
            "experimenter_full_name": ["Person One"],
            "subject_id": "655019",
            "imaging_laser_wavelength": 920,
            "fov_imaging_depth": 200,
            "fov_targeted_structure": "M1",
            "notes": None,
        }
        mock_session_data = {
            "describedBy": (
                "https://raw.githubusercontent.com/AllenNeuralDynamics"
                "/aind-data-schema/main/src/aind_data_schema/core/"
                "session.py"
            ),
            "schema_version": "1.0.3",
            "experimenter_full_name": ["Person One"],
            "session_start_time": "2023-03-22T15:10:35.604999-07:00",
            "session_end_time": "2023-03-22T15:21:33.039442-07:00",
            "session_type": "BCI",
            "iacuc_protocol": "2109",
            "rig_id": "442 Bergamo 2p photostim",
            "subject_id": "655019",
            "mouse_platform_name": "Standard Mouse Tube",
            "active_mouse_platform": False,
            "notes": None,
        }
        mock_run_etl_job.return_value = {
            "status_code": 200,
            "message": "No validation errors detected.",
            "data": json.dumps(mock_session_data),
        }

        response = client.post("/bergamo", json=post_request_content)
        mock_run_etl_job.assert_called_once()
        assert 200 == response.status_code


if __name__ == "__main__":
    pytest.main([__file__])
