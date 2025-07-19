"""Module to handle endpoint responses"""

from aind_metadata_mapper.bergamo.session import (
    BergamoEtl,
)
from aind_metadata_mapper.bergamo.session import (
    JobSettings as BergamoJobSettings,
)
from fastapi import APIRouter, status

from aind_session_json_service_server.models import HealthCheck

router = APIRouter()


@router.get(
    "/healthcheck",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def get_health() -> HealthCheck:
    """
    ## Endpoint to perform a healthcheck on.

    Returns:
        HealthCheck: Returns a JSON response with the health status
    """
    return HealthCheck()


@router.post(
    "/bergamo",
)
def get_session(job_settings: BergamoJobSettings):
    """
    ## Get Session JSON metadata file.
    """

    etl_job = BergamoEtl(
        job_settings=job_settings,
    )
    response = etl_job.run_job()
    return response
