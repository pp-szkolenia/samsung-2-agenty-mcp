# Samsung – agenty AI i serwery MCP

Projekt szkoleniowy (CodersLab, Samsung, grupa 2). Cel w dwóch etapach:

1. **Serwer MCP** (z czasem możliwe kilka serwerów) udostępniający narzędzia przez HTTP.
2. **Agent AI w Pydantic AI**, który korzysta z narzędzi tego serwera jako klient MCP.

## Stos technologiczny

| Obszar | Technologia |
|---|---|
| Język | Python 3.12+ |
| Menedżer pakietów | `uv` (`pyproject.toml` + `uv.lock`) |
| Serwer MCP | FastMCP |
| Transport | Streamable HTTP, endpoint `http://localhost:8765/mcp` |
| Podgląd / debug | MCP Inspector (`@modelcontextprotocol/inspector`) w Dockerze |
| Agent (etap 2) | Pydantic AI, podłączony do serwera MCP przez HTTP |
| Dostawca LLM | OpenRouter (`OPENROUTER_API_KEY` w `.env`, w Pydantic AI `OpenRouterProvider`) |
| Uruchamianie | Docker Compose |

## Struktura

```
servers/<nazwa>/server.py   # każdy serwer MCP w osobnym katalogu
agent/                      # (etap 2) agent Pydantic AI
Dockerfile                  # obraz serwera MCP
docker-compose.yml          # serwer MCP + Inspector
pyproject.toml              # zależności: fastmcp (core), pydantic-ai (grupa `agent`)
.env                        # wszystkie zmienne środowiskowe (poza gitem, zawiera sekrety)
```

Zależności serwera i agenta są rozdzielone: obraz Dockera instaluje tylko `fastmcp`,
a `pydantic-ai` siedzi w grupie `agent` (lokalnie instalowanej domyślnie przez `uv sync`).

## Uruchomienie

```bash
docker compose up --build     # zmienne z jednego pliku .env (poza gitem, zawiera sekrety)
```

- Serwer MCP: `http://localhost:8765/mcp`
- Inspector: `http://localhost:6374/?MCP_PROXY_AUTH_TOKEN=<INSPECTOR_TOKEN>`
  - Transport Type: **Streamable HTTP**
  - URL: `http://localhost:8765/mcp`, Connection Type: **Via Proxy**
  - Inspector działa z `network_mode: host` i nasłuchuje tylko na loopbacku (odmawia `0.0.0.0`),
    dlatego nie ma mapowania portów, a do serwera łączy się przez `localhost`. Wymaga Linuksa.

Porty hosta (8765, 6374, 6377) można zmienić w `.env` (`MCP_SERVER_PORT`, `INSPECTOR_UI_PORT`, `INSPECTOR_PROXY_PORT`).

Hot reload: `./servers` jest montowany do kontenera, a serwer startuje przez `fastmcp run --reload`,
więc każda zmiana w kodzie restartuje serwer (zmiany w `pyproject.toml`/zależnościach wymagają
`docker compose up --build`). Po przeładowaniu w Inspectorze kliknij Reconnect / List Tools.

Lokalnie bez Dockera: `uv sync` i `uv run python servers/demo/server.py`.

## Konwencje

- Kod, komentarze i docstringi po angielsku; dokumentacja i rozmowa po polsku.
- Zależności dodajemy przez `uv add` (`uv add --group agent ...` dla agenta), nie ręcznie.
- Nowy serwer MCP: nowy katalog w `servers/`, osobna usługa w `docker-compose.yml`.
- Porty wystawiamy tylko na `127.0.0.1`.

## Plan

- [x] Szkielet projektu, minimalny serwer FastMCP (`add`, `greet`, zasób `demo://about`), Docker + Inspector
- [ ] Właściwe narzędzia serwera MCP (do ustalenia)
- [ ] Agent Pydantic AI łączący się z serwerem przez HTTP (`agent/`)
- [ ] Opcjonalnie: kolejne serwery MCP, testy, serwis agenta w Compose
