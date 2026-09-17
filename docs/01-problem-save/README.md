# 1단계: 문제 저장

새 문제/프로젝트를 시작할 때 가장 먼저 채우는 단계. 트랙에 따라 템플릿이 다릅니다.

- [algorithm-track.md](algorithm-track.md) — 알고리즘 문제풀이용 (ICPC 문제 명세 규격 기반)
- [project-track.md](project-track.md) — 실무/사이드 프로젝트용 (GitHub Issue Template 규격 기반)
- [prd-template.md](prd-template.md) — 프로젝트가 커질 때 문제저장+분석을 합친 확장판 (PRD)

## 이 단계에서 지켜야 할 규칙 (IEEE 830 기반)

**IEEE 830**(정식 명칭: *IEEE Recommended Practice for Software Requirements
Specifications*)은 소프트웨어 요구사항 문서의 품질 기준을 정한 표준입니다. 이 저장소
전체(1·2단계)에서 아래 두 규칙을 공통으로 가져다 씁니다.

- 하나의 요구사항/설명 문장에는 하나의 동작만 담는다.
- "빠르다/사용하기 편하다/견고하다" 같은 정성적 표현은 쓰지 않는다. 항상 측정 가능한 숫자로 대체.

## 사용 방법

새 문제/프로젝트가 생기면 해당 트랙 파일을 복사해서 (예: `algorithm-track.md` →
`sessions/2026-09-20-leetcode-42.md` 같은 실제 항목 파일) 채우세요. 이 폴더 안의 파일은
"템플릿 원본"이고, 실제로 쌓이는 항목들은 트랙별 하위 폴더(예: `sessions/`)에 따로 모으는 걸
권장합니다.

> **미해결 사항**: `sessions/` 폴더 구조(파일명 규칙, 트랙별 분리 방식)는 아직 확정된
> 결정이 아닙니다. [ADR-0001](../03-pattern-analysis/adr/0001-storage-and-interface.md)은
> "인터페이스를 파일+스킬 하이브리드로 한다"까지만 결정했고, 실제 파일 배치 규칙은
> [4단계(패턴 구현)](../04-pattern-implementation/README.md)에서 SKILL.md 스켈레톤을 만들
> 때 함께 확정합니다. 그전까지 위 예시(`sessions/날짜-문제명.md`)는 잠정안입니다.
