# 2단계: 문제 분석

문제 저장 단계에서 받은 원문제를, 다섯 단계로 이루어진 파이프라인을 거쳐 실제로 다룰 수
있는 요구사항으로 만듭니다. 각 단계는 서로 다른 검증된 방법론을 씁니다.

## 파이프라인

1. **[수집 (Elicitation)](01-elicitation.md)** — BABOK 9대 기법 중 실용적인 것들로 원자료를
   모은다.
2. **[명세 (EARS)](02-specification-ears.md)** — 기능 요구사항을 5가지 정해진 문형으로만
   쓴다. 모호함과 암묵적 예외 케이스를 제거한다.
3. **[정량화 (Planguage)](03-quantification-planguage.md)** — 비기능 요구사항에
   Scale/Meter/Goal을 부여해 "빠르다/편하다" 같은 표현을 숫자로 바꾼다.
4. **[우선순위 (MoSCoW × Kano)](04-prioritization.md)** — 무엇을 지금 할지(MoSCoW)와
   투자 대비 만족도가 어떻게 오르는지(Kano)를 함께 본다.
5. **[추적 (RTM)](05-traceability.md)** — 요구사항 5개 이상인 프로젝트는 출처→설계→구현→
   테스트 연결을 표로 관리한다.

검증(품질 체크)은 `docs/catalog/checklist.md`를 참조 — 매번 이 체크리스트로 최종 점검합니다.

## 새 프로젝트에 적용할 때: 빈 템플릿

```
### 1. 수집
- 사용한 기법: (문서분석/인터뷰/관찰/프로토타이핑/브레인스토밍/워크숍)
- 수집된 원자료:

### 2. 기능 요구사항 (EARS)
FR1 (패턴: Ubiquitous/Event-driven/State-driven/Unwanted/Optional):
  When/While/If <조건>, the 시스템은 shall <행동>.
  근거:
  충족기준:

### 3. 비기능 요구사항 (Planguage)
범주(FURPS):
  Scale:
  Meter:
  Goal:
  Stretch(선택):

### 4. 우선순위
| ID | MoSCoW | Kano |
|---|---|---|

### 5. 추적 (요구사항 5개 이상일 때만)
| ID | 출처 | 3단계 패턴 | 구현 위치 | 테스트 | 상태 |
|---|---|---|---|---|---|
```

## 적용 예시

이 저장소 자체의 요구사항(FR1~FR3)을 이 파이프라인 전체로 실제 적용한 결과:
→ [applied-example.md](applied-example.md)

> 상태: 초안 확정, 사용자 검토 대기 → 확정되면 [`docs/03-pattern-analysis/`](../03-pattern-analysis/README.md)로 진행
