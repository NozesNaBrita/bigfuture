# BigFuture

BigFuture is an open-source personal productivity platform that unifies tasks from multiple sources (Google Tasks, Asana, Trello) into a single, streamlined interface. It is written in TypeScript using Deno as the backend runtime and React/Vite as the frontend, with PostgreSQL as the database. The goal is to manage and track tasks across platforms, stay productive, and eventually contribute back to the community.

---

## 🧩 MVP Scope

The **Minimum Viable Product (MVP)** of BigFuture includes:

### ✅ Core Features

- **Task Importers**  
  Import tasks from:
  - Google Tasks (by list)
  - Asana (by project and section/group)
  - Trello (by workspace, board, and card)

- **Unified Task Model**  
  Store tasks in a unified structure that includes:
  - Title, description
  - Source platform (Google, Asana, Trello)
  - Task metadata (list, project, board, etc.)
  - Due date, recurrence
  - Comments and checklists

- **Task Viewer**
  - Display imported tasks in a unified UI
  - Allow filtering by source, status, and metadata
  - Support basic search

- **Status Update**
  - Mark tasks as completed in BigFuture
  - Automatically update the status in the original platform via API (Google Tasks, Asana, Trello)

---

### 🛠️ Tech Stack

- **Frontend**: React, Vite, Tailwind, Zustand, NextUI
- **Backend**: Deno (with Oak), PostgreSQL, Redis (for background jobs)
- **ORM**: DenoDB or Obsidian
- **Monorepo Management**: Turborepo
- **Deployment**: DigitalOcean + Kamal (ex-MRSK)
- **CI/CD**: GitHub Actions (planned)

---

## 📂 Project Structure

```
bigfuture/ 
├── apps/ 
│ ├── frontend/ # React + Zustand + Tailwind 
│ └── backend/ # Deno + Oak + PostgreSQL + Redis 
├── packages/
│ ├── shared/ # Shared types and utilities 
│ └── cronjobs/ # Background workers, sync jobs 
├── .github/ # GitHub issue templates and workflows 
├── turbo.json # Turborepo configuration 
└── README.md
```


---

## 🚧 Future (Post-MVP)

- Real-time sync with webhooks or polling
- Task deduplication across platforms
- Editable tasks and comments from BigFuture
- Calendar view and planning dashboard
- Multi-language interface (i18n)
- Public roadmap and open contributor program

---

## 📜 License

MIT — free to use, modify and contribute. Let’s build a better future, together.
