# 4단계: 패턴 구현 (스켈레톤)

> 상태: ✅ 완료 (스켈레톤) — 실전 문제로 검증하는 건 5단계에서 진행

3단계(ADR-0001)에서 선택한 "파일+Claude Code 스킬 하이브리드" 패턴을, 실제 문제 데이터
없이 최소 골격으로 구현해서 구조만 검증하는 단계.

## 방향을 정하는 표준 개념 (트랙별)

- **알고리즘 트랙** → [01-algorithm-track-skeleton.md](01-algorithm-track-skeleton.md) —
  "Make it work, make it right, make it fast" 원칙에 따라 브루트포스부터
- **프로젝트 트랙** → [02-project-track-skeleton.md](02-project-track-skeleton.md) —
  Walking Skeleton(Cockburn) / Tracer Bullet(Hunt & Thomas) / Spike(XP) 세 개념 중
  상황에 맞게 선택. **버릴 코드인지 남길 코드인지**가 핵심 구분 기준

## 만든 것

- [`.claude/skills/dev-workflow/SKILL.md`](../../.claude/skills/dev-workflow/SKILL.md) —
  명령 3개(새 문제 저장 / 패턴 검색 / 회고 반영)의 실행 절차 스켈레톤. 성격상
  [Walking Skeleton](02-project-track-skeleton.md)에 해당 — 버릴 코드가 아니라 5단계에서
  그대로 자라날 골격
- [`docs/01-problem-save/sessions/`](../01-problem-save/sessions/README.md) — 1단계에서
  미해결로 남겨뒀던 세션 폴더 구조를 확정 (`sessions/<트랙파일명>/<날짜>-<슬러그>.md`)

## 스켈레톤 검증 (구조만, 실제 사용 아님)

트랙 자동 인식 로직을 현재 저장소에 대입해 스모크 테스트함:

```
$ for f in docs/01-problem-save/*.md; do ...제외 규칙 적용... done
인식된 트랙: algorithm-track
인식된 트랙: project-track
```

`README.md`, `prd-template.md`가 정확히 제외되고 트랙 2개만 잡힘 — 설계대로 동작.

이어서 **자연어 트리거 없이 SKILL.md 절차를 손으로 따라가는 드라이런**도 진행함
(Two Sum 예시, [세션 파일](../01-problem-save/sessions/algorithm-track/2026-09-17-two-sum.md)):

- 명령 1(문제 저장): 통과 — 트랙 목록 나열 → 필드 채움 → `sessions/algorithm-track/2026-09-17-two-sum.md`로 저장
- 명령 2(패턴 검색): 통과 — 빈 `catalog/patterns.md`에서 검색 실패 시 표준 카탈로그로
  올바르게 폴백함
- 이 드라이런에서 **실제 결함을 하나 발견**: 2단계 5단계 파이프라인이 알고리즘 트랙
  단순 문제엔 과함 → [2단계 README](../02-problem-analysis/README.md)에 "적용 범위"
  절 추가, `catalog/checklist.md`에 회고 항목 추가, SKILL.md 명령 1 step 4 수정으로 해결

## 아직 검증 안 된 것 (5단계로 넘김)

- **자연어 트리거 자체**(스킬 설명文에 맞는 요청을 했을 때 실제로 발동하는지)는 이
  드라이런으로도 확인 못 함 — Claude Code가 세션 시작 시 스킬 목록을 고정하기 때문에,
  이 저장소 경로에서 새 세션을 열어야 확인 가능. Walking Skeleton의 일부가 아니라
  [Spike](02-project-track-skeleton.md) 성격의 불확실성이므로, 5단계에서 짧게 확인만
  하고 넘어간다
- Planguage Usability Goal(템플릿 작성 5분 이내) 실측 — 6단계에서 확인
