# 7단계: 유지보수

> 상태: ⬜ 미착수

이 워크플로우의 핵심 피드백 루프가 일어나는 단계 (원문제: "배운 게 재사용 안 됨"을
해결하는 지점).

## 회고 템플릿

```
날짜:
문제/프로젝트:
잘된 점:
어려웠던 점:
  → 5 Whys (왜 이 문제가 생겼는가, 근본원인까지 파고들기):
    1. 왜?
    2. 왜?
    3. 왜? (근본원인에 도달할 때까지 반복, 보통 3~5회)
새로 배운 패턴 (있다면) → catalog/patterns.md에 추가:
놓쳤던 체크리스트 항목 (있다면) → catalog/checklist.md에 추가:
```

**"어려웠던 점"에 5 Whys를 쓰는 이유**: 도요타 생산방식에서 나온 근본원인 분석 기법으로,
"왜?"를 반복해서 표면 증상이 아니라 구조적 원인까지 파고듭니다. 예를 들어 "엣지 케이스를
놓쳤다"에서 멈추지 않고 "왜 놓쳤나 → 체크리스트에 그 항목이 없었다 → 왜 없었다 →
비슷한 실수를 처음 겪어봤다"까지 가야, `catalog/checklist.md`에 추가할 항목이
명확해집니다.

## 원칙: Blameless (무결점 추궁이 아니라 시스템 원인 찾기)

Etsy CTO였던 John Allspaw가 2012년에 정립하고 이후 Google SRE가 표준 관행으로 채택한
**Blameless Postmortem** 원칙입니다. 핵심: "이번엔 왜 놓쳤지, 내가 부주의했나"처럼
사람을 탓하는 방향으로 5 Whys를 몰고 가면 안 됩니다. 관련된 모든 행동이 **그 순간 알고
있던 정보로는 합리적이었다**고 가정하고, "왜?"의 답은 항상 **시스템/프로세스의 빈틈**
쪽으로 향해야 합니다.

- 나쁜 예: "왜 놓쳤나? → 내가 집중을 안 해서" (사람 탓 — 여기서 멈추면 재발 방지가 안 됨)
- 좋은 예: "왜 놓쳤나? → 체크리스트에 그 항목이 없어서 확인할 방법 자체가 없었다"
  (시스템 탓 — `checklist.md`에 항목을 추가하면 다음엔 안 놓침)

개인 프로젝트에서도 이 원칙은 똑같이 유효합니다 — "내가 못해서"로 끝내면 아무 것도
바뀌지 않고, "이 구조에 무슨 구멍이 있었나"로 끝내야 `catalog/`가 실제로 자랍니다.

## 절차 (UC7 참조)

1. 회고 작성 (위 템플릿, 5 Whys로 근본원인까지 파고들기)
2. "새로 배운 패턴" 항목이 있으면 [`docs/catalog/patterns.md`](../catalog/patterns.md)에
   Volere 카드 형식으로 추가
3. "놓쳤던 체크리스트 항목"이 있으면 (5 Whys의 근본원인을 그대로 반영해서)
   [`docs/catalog/checklist.md`](../catalog/checklist.md)에 추가
4. git 커밋으로 이력 남기기 (커밋 메시지에 어떤 프로젝트/문제에서 나온 교훈인지 명시)

이 단계를 건너뛰면 다음 프로젝트의 [2단계](../02-problem-analysis/README.md)·
[3단계](../03-pattern-analysis/README.md)가 과거 경험을 참조하지 못합니다 — 원문제가
재발합니다.

## 출처
- [Five whys - Wikipedia](https://en.wikipedia.org/wiki/Five_whys) — Sakichi Toyoda,
  도요타 생산방식(1930년대)에서 유래한 근본원인 분석 기법
- Allspaw, J., *Blameless PostMortems and a Just Culture* (2012, Etsy) —
  [Google SRE Book: Postmortem Culture](https://sre.google/sre-book/postmortem-culture/)
