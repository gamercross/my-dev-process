# 나만의 개발 워크플로우 시스템

문제 저장 → 문제 분석 → 패턴 분석 → 패턴 구현 → 구현 → 서비스 → 유지보수, 7단계로
새 프로그램/프로젝트를 진행하기 위한 개인 워크플로우 저장소.

내용은 단계별로 `docs/` 아래 나뉘어 있습니다. 특정 단계를 수정할 때는 그 단계 폴더의
md 파일만 고치면 됩니다.

## 새 일이 생기면 (퀵스타트)

1. **규모부터 정한다** → [docs/00-overview/scope-tiers.md](docs/00-overview/scope-tiers.md)
   — 2~5분짜리면 그냥 바로 처리, 아니면 Full/Xpress/Lite 중 하나
2. **Claude Code에서 `dev-workflow` 스킬을 트리거**한다 ("새 문제 시작" 등) —
   [`.claude/skills/dev-workflow/SKILL.md`](.claude/skills/dev-workflow/SKILL.md)가
   트랙 선택부터 저장까지 안내함. 스킬 없이 수동으로 하려면
   [docs/01-problem-save/](docs/01-problem-save/README.md) 템플릿을 직접 채운다
3. 단계를 넘어갈 때마다 → [docs/00-overview/gates.md](docs/00-overview/gates.md)의
   DoR/DoD로 확인

## 더 알아보려면

**전체 그림: [docs/00-overview/README.md](docs/00-overview/README.md)** — 원문제 정의, 전체
방향 다이어그램, 진행상황, 유즈케이스.

**게이트 규정: [docs/00-overview/gates.md](docs/00-overview/gates.md)** — 단계별
진입기준(DoR)/완료기준(DoD)과 Go·Kill·Hold·Recycle 게이트 규정, 개별 문제용 게이트
로그 템플릿.

## 폴더 구조

```
.claude/skills/dev-workflow/   Claude Code 스킬 — 새 문제 저장 / 패턴 검색 / 회고 반영
                                3개 명령의 실행 절차 (Walking Skeleton)
docs/
  00-overview/                 원문제, 전체 다이어그램, 진행상황, 유즈케이스
                                + gates.md(게이트 규정) + scope-tiers.md(규모 판단)
  01-problem-save/             1단계: 문제 저장 템플릿(트랙별 + PRD)
                                + sessions/(실제로 채운 문제/프로젝트 항목이 쌓이는 곳)
  02-problem-analysis/         2단계: 요구사항 분석 방법론(BABOK/EARS/Planguage/Kano/RTM)
                                + 적용 범위(트랙별 경량화 규칙) + 적용 예시
  03-pattern-analysis/         3단계: 패턴/아키텍처 선택 (CLRS 패러다임 / 아키텍처 5대
                                스타일 / ATAM) + adr/(Architecture Decision Record)
  04-pattern-implementation/   4단계: 패턴 스켈레톤 (Walking Skeleton / Tracer Bullet /
                                Spike) + 다이어그램 선택 가이드
  05-implementation/           5단계: TDD Red-Green-Refactor + 동등분할·경계값 분석
  06-service/                  6단계: Twelve-Factor App (배포) + Planguage Goal 실측
  07-maintenance/              7단계: 회고 (5 Whys + Blameless Postmortem)
  catalog/                     patterns.md(패턴 카탈로그) + checklist.md(분석
                                체크리스트) — 7단계 회고에서 계속 누적되는 공용 자료
```
