# Backend Dependency Updates

This backend service owns the SQLAlchemy models and is expected to drive Alembic migrations.

DB Tooling alignment:
- See database container notes at: ../delivery-tracker-pro-224135-224145/database/DB_DEPENDENCY_UPDATES.md
- Recommended pinned versions for DB tooling:
  - Alembic: 1.13.2
  - SQLAlchemy: 2.0.36
  - psycopg (psycopg3): 3.2.3 (preferred) or psycopg2-binary: 2.9.10

Actions for backend:
- Pin the above versions in backend requirements.
- Configure Alembic in the backend to point to the same database URL (DATABASE_URL).
- Generate and apply migrations from the backend repository.
