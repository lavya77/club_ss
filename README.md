# 🎓 Club Management System Backend

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-4.x-green)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.20-blueviolet)](https://www.django-rest-framework.org/)
[![License](https://img.shields.io/badge/license-MIT-brightgreen)](LICENSE)

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Models](#models)
5. [Serializers](#serializers)
6. [API Endpoints](#api-endpoints)
7. [Permissions](#permissions)
8. [Setup Instructions](#setup-instructions)
9. [Example API Calls](#example-api-calls)
10. [Future Enhancements](#future-enhancements)

---

## Project Overview
Club Management System is a Django backend for managing university clubs, events, announcements, and memberships. It implements **role-based access control** with **Admin**, **Club Head**, and **Student** roles. Built with **Django REST Framework (DRF)**, it provides clean and scalable APIs.

---

## Features
- Role-based access (Admin, Club Head, Student)
- CRUD operations for:
  - Clubs
  - Club Types
  - Events
  - Announcements
  - Memberships
- Nested endpoints for related objects
- Custom permissions for Club Head & Admin
- JWT or Token-based authentication support (optional)

---

## Tech Stack
- **Backend:** Django 4.x  
- **API:** Django REST Framework (DRF)  
- **Database:** PostgreSQL / SQLite (Development)  
- **Authentication:** Django default User model with `role` field  
- **Testing:** DRF Browsable API  

---

## Models

### ClubType
| Field     | Type      | Description                  |
|-----------|-----------|------------------------------|
| club_type | CharField | Name of the club type        |

### Club
| Field       | Type       | Description                  |
|-------------|-----------|------------------------------|
| club_name   | CharField | Name of the club             |
| club        | ForeignKey| Club type (ClubType)         |
| description | TextField | Club description             |

### Event
| Field        | Type       | Description                  |
|--------------|-----------|------------------------------|
| name         | CharField | Event name                   |
| organised_by | ForeignKey| Club hosting the event       |

### Announcements
| Field             | Type       | Description                  |
|-------------------|-----------|------------------------------|
| Announcements_name | CharField | Announcement title          |
| description       | TextField | Announcement description     |
| club_related      | ForeignKey| Club related to announcement |

### Membership
| Field       | Type       | Description                  |
|-------------|-----------|------------------------------|
| user        | ForeignKey| User of the system           |
| club        | ForeignKey| Club the user joined         |
| role        | CharField | Role (Member, Club Head)     |
| date_joined | DateTimeField | Join date                 |

---

## Serializers
- `ClubSerializer` – Club model  
- `ClubtypeSerializer` – ClubType model  
- `EventSerializer` – Event model  
- `AnnouncementsSerializer` – Announcements model  
- `MembershipSerializer` – Membership model  

Supports **nested serializers** for retrieving related objects.

---

## API Endpoints

### ClubType
| Method | Endpoint        | Permissions | Description          |
|--------|----------------|------------|--------------------|
| GET    | `/api/clubtypes/` | Public     | List all club types |
| POST   | `/api/clubtypes/` | Admin      | Create new club type |

### Club
| Method | Endpoint       | Permissions | Description       |
|--------|---------------|------------|-----------------|
| GET    | `/api/clubs/` | Public      | List all clubs   |
| POST   | `/api/clubs/` | Admin       | Create new club  |
| PUT/PATCH/DELETE | `/api/clubs/{id}/` | Admin | Update/Delete club |

### Event
| Method | Endpoint         | Permissions          | Description            |
|--------|----------------|-------------------|----------------------|
| GET    | `/api/events/` | All authenticated   | List events           |
| POST   | `/api/events/` | Club Head / Admin   | Create event          |
| PUT/PATCH/DELETE | `/api/events/{id}/` | Club Head / Admin | Update/Delete event |
| GET    | `/api/events/{id}/events/` | Authenticated | Nested events for a club |

### Announcements
| Method | Endpoint                | Permissions         | Description              |
|--------|------------------------|------------------|-------------------------|
| GET    | `/api/announcements/`  | All users         | List announcements      |
| POST   | `/api/announcements/`  | Club Head / Admin | Create announcement     |
| PUT/PATCH/DELETE | `/api/announcements/{id}/` | Club Head / Admin | Update/Delete announcement |

### Membership
| Method | Endpoint            | Permissions         | Description                |
|--------|-------------------|------------------|---------------------------|
| GET    | `/api/memberships/` | All users         | List memberships          |
| POST   | `/api/memberships/` | Admin / Club Head | Create membership         |
| PUT/PATCH/DELETE | `/api/memberships/{id}/` | Admin / Club Head | Update/Delete membership |

---

## Permissions
- **IsAuthenticated** – Ensure user is logged in  
- **IsClubHeadOrReadOnly** – Custom permission:
  - Club Heads can create events and announcements  
  - Others have read-only access  
- **Admin** – Full access

---

## Setup Instructions

1. **Clone repository**
```bash
git clone <repo-url>
cd club-management-backend
