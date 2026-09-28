# 외부 스킬 / MCP 도구 카탈로그

`dev-workflow` 바깥에서 가져온 공식 스킬·플러그인·MCP 서버를 추적합니다.
분석·판정 절차는 [`.claude/rules/external-integration.md`](../../.claude/rules/external-integration.md)를
따릅니다 — 이 표는 그 결과만 기록하는 곳입니다.

## 카탈로그

| 이름 | 출처 | 붙인 목적 | 우리 파일 건드림? | 판정 | 근거 |
|---|---|---|---|---|---|
| `update-config` | Claude Code 번들 스킬(`bundled:update-config`) | `.claude/settings.json`의 훅 구성을 안전하게 작성(읽기→병합→pipe-test→`jq` 검증→실제 발화 증명 절차 제공) | `.claude/settings.json`만. "항상 기존 설정을 먼저 읽고 병합, 배열은 교체하지 않고 추가" 원칙이 있어 `.claude/rules/**`·`hooks/**` 본문·`CLAUDE.md`는 건드리지 않음 | 채택 | 2026-09-17 인프라 신설 때 이 스킬의 dedup-check→pipe-test→`jq -e` 검증→실제 발화 확인 절차를 그대로 따라 `block-dangerous-git.sh` 등 3개 훅을 등록했음(사후 분석). `settings.json` 외 기준 파일에 손대지 않아 우리 rules/hooks/agents와 충돌 없음 확인 — 새 라우팅 표 행은 불필요(이미 `consistency.md`의 hooks 행이 `settings.json`을 커버) |

## 판정 기준

- **채택** — 우리 rules/hooks/agents 체계에 정식으로 편입. `CLAUDE.md` 라우팅
  표와 `.claude/rules/consistency.md`의 기준 파일 지도에도 반영됨.
- **격리** — 자기 폴더 밖의 어떤 파일도 건드리지 않는다는 게 확인된 채로,
  독립적으로만 동작. 우리 라우팅 표·기준 파일 지도는 그대로.
- **제거** — 실효성 없음 또는 충돌 확인 → 삭제, 근거만 남김.
