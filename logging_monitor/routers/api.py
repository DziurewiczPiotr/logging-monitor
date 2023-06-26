from fastapi import APIRouter, status
from logging_monitor.consts import ROOT_DIR
from tomli import load
from logging_monitor.view_models import AppMeta, Log, Logs

router = APIRouter()

log_container: Logs = []


@router.get("/", status_code=status.HTTP_200_OK, tags=["api"])
def app_meta():
    with open(ROOT_DIR / "pyproject.toml", "rb") as file:
        pyproject = load(file)["tool"]["poetry"]

    meta = AppMeta(
        name=pyproject.get("name"),
        version=pyproject.get("version"),
        description=pyproject.get("description"),
        authors=pyproject.get("authors"),
    )

    return meta


@router.post("/log", status_code=status.HTTP_201_CREATED, tags=["api"])
def add_single_log(log: Log):
    log_container.append(log)
    return log


@router.get("/logs", status_code=status.HTTP_200_OK, tags=["api"])
def get_all_logs():
    return log_container
