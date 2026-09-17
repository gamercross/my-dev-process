# 비기능 요구사항 정량화 — Gilb's Planguage

기존 FURPS+ 규칙("정성적 표현 금지, 측정 가능한 숫자로")은 원칙만 말해주고 "어떻게
숫자로 만드는가"는 안 알려줍니다. Tom Gilb의 **Planguage**는 "정량화할 수 없으면 통제할
수 없다(If you can't quantify it, you can't control it)"는 원칙 아래, 비기능 요구사항을
정확히 숫자로 못박는 표준 필드를 제공합니다.

## Planguage 핵심 필드

| 필드 | 의미 |
|---|---|
| Scale | 측정 단위 (예: "초", "%", "MB") |
| Meter | 실제로 어떻게 측정할 것인가 (예: "stopwatch로 측정", "git log 커밋 시각 차이") |
| Past | 현재/과거 수준 (baseline) |
| Goal | 이번에 달성해야 하는 최소 기준 (이걸 못 채우면 요구사항 미충족) |
| Stretch | 더 바람직한 수준 |
| Wish | 이상적이지만 지금 당장은 무리인 수준 |

## 우리 프로젝트 NFR을 Planguage로 재작성

기존 FURPS+ 표의 막연했던 항목들을 아래처럼 못박습니다.

### Usability — "각 단계 템플릿은 5분 이내 작성 가능"

```
Scale: 템플릿 1개 작성에 걸리는 시간(분)
Meter: 실제로 타이머를 켜고 템플릿을 채워보며 측정
Past: (아직 측정 안 함 — 최초 사용 시 기록)
Goal: 5분 이내
Stretch: 3분 이내
```

### Supportability — "새 트랙 추가 시 기존 구조 무변경으로 확장 가능"

```
Scale: 새 트랙 추가 시 수정해야 하는 기존 파일 수(개)
Meter: git diff로 새 트랙 추가 커밋에서 변경된 기존 파일 수를 센다
Goal: 0개 (신규 파일만 추가)
Stretch: 해당 없음 (0이 이미 최선)
```

### Reliability — "저장 데이터 유실 방지"

```
Scale: 데이터 유실 사고 건수
Meter: git log 이력 확인 (force-push, reset --hard 등 이력 파괴 행위 여부)
Goal: 0건
Wish: 모든 변경 이력이 영구 보존됨 (git 자체가 이미 이 조건을 만족)
```

## 이 저장소에서의 규칙

- 비기능 요구사항(FURPS+ 표)에는 최소한 `Scale`, `Meter`, `Goal` 세 필드를 반드시 채운다.
- "빠르다/편하다/견고하다" 같은 표현이 나오면 반드시 이 문서 형식으로 재작성한다.

## 출처
- Gilb, T., *Specifying Quality Requirements With Planguage*, [ModernAnalyst](https://www.modernanalyst.com/Resources/Articles/tabid/115/ID/2926/Specifying-Quality-Requirements-With-Planguage.aspx)
- Gilb, T., *How to Quantify Quality: Finding Scales of Measure*, [ACCU Overload 13(70)](https://www.accu.org/journals/overload/13/70/gilb_299/)
