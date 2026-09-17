# 요구사항 수집 (Elicitation)

명세를 쓰기 전에, 먼저 "무엇을 요구사항으로 뽑아낼지"부터 의식적으로 수집해야 합니다.
IIBA(국제비즈니스분석협회)의 BABOK(Business Analysis Body of Knowledge) 가이드가 정의한
9가지 핵심 수집 기법 중, 개인 프로젝트에 실용적인 것들:

## 핵심 기법

| 기법 | 언제 쓰는가 | 개인 워크플로우 적용 |
|---|---|---|
| Document Analysis (문서 분석) | 기존 자료(이슈, 이전 코드, 레퍼런스 문서)가 있을 때 | 1단계 문제 저장 항목, 과거 `catalog/` 참고 |
| Interview (인터뷰) | 이해관계자가 있을 때 | 실무 프로젝트에서 요청자/사용자와 대화 |
| Observation (관찰) | 실제 사용 흐름을 봐야 할 때 | 기존 시스템/코드가 실제로 어떻게 쓰이는지 관찰 |
| Prototyping (프로토타이핑) | 요구사항이 모호할 때 | 최소 스켈레톤을 먼저 만들어보고 요구사항을 역으로 발견 (4단계와 연결) |
| Brainstorming | 초기 아이디어 발산 | 문제를 처음 만났을 때 후보 해석 여러 개 나열 |
| Requirements Workshop | 여러 요구사항을 한 번에 정리·우선순위화할 때 | 개인 프로젝트에선 "혼자 하는 워크숍" — 2단계 전체를 한 세션에 몰아서 진행 |

## 권장 순서 (BABOK 실무 관행)

**문서 분석 → 인터뷰/관찰 → 워크숍(정리·우선순위화)** 순으로 진행하는 게 일반적입니다.
개인 프로젝트에서는:

1. 1단계에서 저장한 문제 항목 + `catalog/patterns.md`, `catalog/checklist.md`를 먼저 검토
   (Document Analysis)
2. 실무 프로젝트라면 실제 요청자/사용자 확인 (Interview), 혼자 하는 프로젝트라면 유사
   사례 관찰 (Observation)
3. 나온 후보들을 [02-specification-ears.md](02-specification-ears.md) 형식으로 정리
   (Workshop 역할)

## 출처
- IIBA BABOK Guide, [4.2 Conduct Elicitation](https://www.iiba.org/knowledgehub/business-analysis-body-of-knowledge-babok-guide/4-elicitation-and-collaboration/4.2-conduct-elicitation)
