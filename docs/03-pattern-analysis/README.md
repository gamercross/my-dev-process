# 3단계: 패턴 분석

2단계에서 확정된 요구사항을 놓고, 어떤 패턴/아키텍처로 풀지 후보를 비교해 결정하는 단계.
트랙에 따라 쓰는 도구가 다릅니다.

## 알고리즘 트랙

- [`docs/catalog/patterns.md`](../catalog/patterns.md)에서 태그가 일치하는 항목 검색
- 후보가 여러 개면 트레이드오프(시간복잡도, 구현 난이도)를 표로 비교
- 선택 근거를 한 줄이라도 남긴다 (7단계 회고에서 "왜 이걸 골랐는지" 복기 가능하게)

## 프로젝트 트랙 — ADR (Architecture Decision Record)

아키텍처/구조 선택처럼 오래 남아야 하는 결정은 Michael Nygard가 제안한 **ADR** 포맷으로
기록합니다. 소프트웨어 업계 표준 관행이며 AWS·Azure·Google Cloud 팀들도 이 포맷을 씁니다.

### ADR 템플릿

```
# ADR-000X: <결정 제목>

- Status: Proposed / Accepted / Rejected / Deprecated / Superseded
- Date:

## Context
(어떤 문제/제약 때문에 이 결정이 필요한가 — 2단계 요구사항 인용)

## Decision
(무엇을 하기로 했는가)

## Considered Alternatives
(고려했지만 채택 안 한 대안과 기각 이유)

## Consequences
(이 결정으로 생기는 장단점, 특히 나중에 발목 잡을 수 있는 것)
```

### 이 저장소의 ADR 목록

- [ADR-0001: 워크플로우 인터페이스를 파일+Claude Code 스킬 하이브리드로 결정](adr/0001-storage-and-interface.md)

## 출처
- Nygard, M., *Documenting Architecture Decisions* (2011) — [원문 포맷 정리](https://github.com/joelparkerhenderson/architecture-decision-record/blob/main/locales/en/templates/decision-record-template-by-michael-nygard/index.md)
- [Architectural Decision Records](https://adr.github.io/)
