from fastapi import FastAPI
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# PUBLIC_INTERFACE
class AppSettings(BaseSettings):
    """Application settings loaded from environment variables via pydantic-settings."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    app_name: str = Field(default="Delivery Tracker Backend", description="Human-readable application name")
    debug: bool = Field(default=False, description="Enable debug mode")

# PUBLIC_INTERFACE
class HealthResponse(BaseModel):
    """Simple health response model."""

    status: str = Field(..., description="Service status string")
    app: str = Field(..., description="Application name")
    version: str = Field(..., description="API version label")

def create_app() -> FastAPI:
    """Factory to create FastAPI app with metadata and tags."""
    settings = AppSettings()

    app = FastAPI(
        title=settings.app_name,
        description="Backend API for real-time delivery tracking, authentication, and notifications.",
        version="0.1.0",
        contact={"name": "Delivery Tracker", "email": "support@example.com"},
        license_info={"name": "MIT"},
        openapi_tags=[
            {"name": "health", "description": "Service health and diagnostics"},
        ],
    )

    @app.get(
        "/health",
        response_model=HealthResponse,
        summary="Health check",
        description="Returns basic service health details.",
        tags=["health"],
        responses={200: {"description": "Service is healthy"}},
    )
    # PUBLIC_INTERFACE
    def health() -> HealthResponse:
        """Health endpoint returning status, app name, and version."""
        return HealthResponse(status="ok", app=settings.app_name, version=app.version)

    return app

app = create_app()
