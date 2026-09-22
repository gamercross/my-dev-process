# 세션 (실제로 채운 문제/프로젝트 항목)

이 폴더는 `docs/01-problem-save/`의 템플릿 파일(`algorithm-track.md`, `project-track.md`)을
실제로 채운 결과물이 쌓이는 곳입니다. 템플릿 원본은 건드리지 않고, 여기에 트랙별 하위
폴더를 만들어 항목을 모읍니다.

## 경로 규칙 (4단계에서 확정, `.claude/skills/dev-workflow/SKILL.md` 참고)

```
docs/01-problem-save/sessions/<트랙파일명(확장자 제외)>/<YYYY-MM-DD>-<슬러그>.md
```

예: `docs/01-problem-save/sessions/algorithm-track/2026-09-20-two-sum.md`

트랙파일명은 `docs/01-problem-save/`에 있는 템플릿 파일 이름과 그대로 맞춥니다 —
새 트랙(`README.md`, `prd-template.md`가 아닌 새 `*.md` 파일)을 추가하면 이 폴더에도
같은 이름의 하위 폴더가 자연스럽게 생깁니다.

## 트래커 — 지금까지 진행한 모든 항목

새 항목을 저장하거나 게이트가 바뀔 때마다 이 표를 같이 갱신합니다. 개별 항목의
자세한 진행(게이트 로그, 회고)은 각 세션 파일에, 실제 코드/테스트는
[`implementations/`](../../../implementations/)에 있습니다.

| 문제/프로젝트 | 트랙 | 등급 | 사용한 패턴 | 게이트 | 테스트 | 세션 파일 |
|---|---|---|---|---|---|---|
| Two Sum | 알고리즘 | Xpress | 해시맵 원패스 탐색 | 1→7 완주 | 5개 | [보기](algorithm-track/2026-09-17-two-sum.md) |
| Contains Duplicate | 알고리즘 | Xpress | 해시맵 원패스 탐색 | 1→7 완주 | 6개 | [보기](algorithm-track/2026-09-17-contains-duplicate.md) |
| Valid Parentheses | 알고리즘 | Xpress | 스택 기반 매칭 (신규) | 1→7 완주 | 7개 | [보기](algorithm-track/2026-09-19-valid-parentheses.md) |
| 카탈로그 검색 CLI | 프로젝트 | Full | Layered (ADR-0002) | 1→7 완주 | 6개 | [보기](project-track/2026-09-19-catalog-search-cli.md) |
| Contains Duplicate II | 알고리즘 | Xpress | 해시맵 원패스 탐색 (3번째 재사용) | 1→7 완주 | 7개 | [보기](algorithm-track/2026-09-19-contains-duplicate-ii.md) |
| Best Time to Buy and Sell Stock | 알고리즘 | Xpress | 한 번 순회 최솟값 추적 (신규, 그리디) | 1→7 완주 | 7개 | [보기](algorithm-track/2026-09-22-best-time-to-buy-and-sell-stock.md) |
| 진행상황 대시보드 생성기 | 프로젝트 | Full | Microkernel (ADR-0003) + 환경변수 기반 Config 오버라이드 (재사용) | 1→7 완주 | 10개 | [보기](project-track/2026-09-22-progress-dashboard-generator.md) |
| Conventional Commits | 학습 | Lite | - | 1→7 완주 | - | [보기](learning-track/2026-09-22-conventional-commits.md) |

전체 테스트를 한 번에 돌리려면: `python3 implementations/run_all_tests.py`

## 지금까지 나온 패턴/교훈이 남는 곳

- **패턴**: [`docs/catalog/patterns.md`](../../catalog/patterns.md) — 위 표의 "사용한 패턴" 열이 여기서 옵니다
- **체크리스트**: [`docs/catalog/checklist.md`](../../catalog/checklist.md) — 회고에서 나온 재발 방지 항목
- **과정 전체 기록**: [`docs/00-overview/worklog.md`](../../00-overview/worklog.md)
