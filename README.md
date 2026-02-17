# Distributed-rate-limiter
Full-stack distributed rate limiting platform built with FastAPI, React, and Redis, featuring sliding window algorithms and real-time monitoring dashboard

This project simulates a lightweight API gateway similar to those used in production systems to prevent abuse, enforce request quotas, and monitor traffic patterns.

Frontend Dashboard: In Progress
Backend API: In Progress

# Architecture Overview

Client → FastAPI Backend → Redis (distributed counters)
React Dashboard → Backend Metrics Endpoint

backend enforces rate limiting using a sliding window backed by Redis operations

# Tech Stack

Backend
- Python
- FastAPI
- Redis (Upstash)
- Pydantic (validation)
- Uvicorn

Frontend
- React (Vite)
- Axios
- Lightweight dashboard UI

Deployment
- Render (Backend)
- Vercel (Frontend)
- Upstash (Redis)

# Core Features
- Distributed sliding window rate limiting
- Per user API key enforcement
- Redis-backed atomic counters
- Real time usage metrics endpoint
- Structured logging
- Configurable request thresholds
