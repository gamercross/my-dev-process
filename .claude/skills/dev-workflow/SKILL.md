---
name: dev-workflow
description: 새 문제/프로젝트를 저장하거나, 과거 패턴을 검색하거나, 회고를 카탈로그에 반영할 때 쓰는 개인 7단계 개발 워크플로우 스킬. "새 문제 시작", "이 프로젝트 저장해줘", "비슷한 패턴 있어?", "회고 작성", "이번에 배운 거 반영해줘" 같은 요청에 반응한다.
---

# 개인 개발 워크플로우 (dev-workflow)

이 스킬은 이 저장소(`my-dev-process`)의 `docs/` 구조를 대신 다뤄주는 **실행 절차**만
담습니다. 방법론 자체(왜 이렇게 하는지, 어떤 표준을 근거로 하는지)는 각
`docs/0X-*/README.md`를 참고하세요.

> 상태: 스켈레톤(4단계 산출물). 실제 문제로 검증하는 건 5단계에서 진행합니다.

## 트랙 자동 인식 (ADR-0001의 Supportability 제약 반영)

`docs/01-problem-save/` 안에서 **`README.md`와 `prd-template.md`를 제외한 모든 `*.md`
파일**이 하나의 "트랙 템플릿"입니다. 지금은 `algorithm-track.md`, `project-track.md` 2개.
새 트랙을 추가하고 싶으면 이 폴더에 파일 하나만 추가하면 되고, **이 스킬의 로직·문구를
바꿀 필요가 없습니다** — 항상 그 순간의 폴더 내용을 다시 나열하세요.

## 명령 1: 새 문제/프로젝트 저장 (1단계)

1. **먼저 규모를 정한다** ([`docs/00-overview/scope-tiers.md`](../../../docs/00-overview/scope-tiers.md)):
   전체가 2~5분 안에 끝나면 **즉시처리**로 아무 단계도 안 밟고 끝낸다. 그 외엔
   Xpress/Lite/Full 중 하나를 정하고 이후 단계에 반영한다.
2. `docs/01-problem-save/`에서 위 규칙으로 트랙 템플릿 목록을 나열하고, 트랙이 2개
   이상이면 사용자에게 고르게 한다. 트랙이 1개뿐이면 자동 선택.
3. 선택한 템플릿 파일의 필드를 사용자와 함께 채운다. 필수 필드가 비어 있으면 다음
   단계로 넘어가지 않는다 (1단계 IEEE 830 규칙 — 하나의 문장에 하나의 동작, 정성적
   표현 금지). **Full 등급 + 프로젝트 트랙이면** 여기서
   [`docs/01-problem-save/prd-template.md`](../../../docs/01-problem-save/prd-template.md)로
   확장할지도 물어본다 — 확장하면 PRD 섹션도 같이 채운다.
4. 완성된 내용을 아래 규칙으로 저장한다 (1단계에서 미해결로 남겨뒀던 세션 폴더 구조의
   확정판):

   ```
   docs/01-problem-save/sessions/<트랙파일명(확장자 제외)>/<YYYY-MM-DD>-<슬러그>.md
   ```

   예: `docs/01-problem-save/sessions/algorithm-track/2026-09-20-two-sum.md`

5. 저장한 세션 파일 맨 아래에
   [`docs/00-overview/gates.md`](../../../docs/00-overview/gates.md)의 "새 문제/
   프로젝트용 게이트 로그 템플릿" 블록을 붙여서 시작한다 (등급 줄부터 채우고 1→2
   게이트부터 진행). 이게 없으면 이 문제가 어느 게이트까지 통과했는지 남길 곳이 없다.
6. 저장 후 다음을 확인한다: **알고리즘 트랙의 단순 문제는 보통 2단계를 생략하고 바로
   [3단계 패턴 분석](../../../docs/03-pattern-analysis/README.md)으로 간다** — 2단계의
   5단계 파이프라인(BABOK/EARS/Planguage/Kano/RTM)은 무거운 프로젝트 트랙용이다
   ([`docs/02-problem-analysis/README.md`](../../../docs/02-problem-analysis/README.md)의
   "적용 범위" 참고). 프로젝트 트랙이거나 문제가 복잡하면 [2단계](../../../docs/02-problem-analysis/README.md)로.

## 명령 2: 패턴 검색 (3단계)

1. 사용자가 준 키워드/태그로 `docs/catalog/patterns.md`를 검색한다 (grep 방식).
2. 일치하는 항목이 있으면 각 항목의 "언제 쓰는가"/"트레이드오프"를 요약해 보여준다.
3. 없으면 표준 카탈로그로 안내한다 — 알고리즘 트랙은
   `docs/03-pattern-analysis/01-algorithm-paradigms.md`(설계 패러다임 + 구현 기법 패턴
   두 계층 모두 확인), 프로젝트 트랙은
   `docs/03-pattern-analysis/02-architecture-styles.md`.

## 명령 3: 회고를 카탈로그/체크리스트에 반영 (7단계)

1. `docs/07-maintenance/README.md`의 회고 템플릿으로 사용자와 함께 채운다 —
   "어려웠던 점"은 **5 Whys**로 근본원인까지 파고든다 (표면 증상에서 멈추지 않는다).
2. "새로 배운 패턴"이 나오면 `docs/catalog/patterns.md`에 기존 Volere 카드 형식 그대로
   추가한다.
3. "놓쳤던 체크리스트 항목"이 나오면 (5 Whys의 근본원인을 반영해서)
   `docs/catalog/checklist.md`에 추가한다.
4. 변경 사항을 git commit한다 — 커밋 메시지에 어떤 프로젝트/문제에서 나온 교훈인지 명시.

## 이 스킬이 하지 않는 것 (ADR-0001 Consequences 참고)

- 자체적으로 자동 테스트를 돌리지 않는다 — Usability Goal(템플릿 작성 5분 이내)은
  사용자가 실제로 써보며 수동으로 확인한다 ([6단계](../../../docs/06-service/README.md)
  "Planguage Goal 실측" 참고).
- Claude Code 밖에서는 동작하지 않는다 — 다른 환경에서는 `docs/`를 사람이 직접 읽고 쓴다.
