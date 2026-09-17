# 나만의 개발 워크플로우 시스템

문제 저장 → 문제 분석 → 패턴 분석 → 패턴 구현 → 구현 → 서비스 → 유지보수, 7단계로
새 프로그램/프로젝트를 진행하기 위한 개인 워크플로우 저장소.

내용은 단계별로 `docs/` 아래 나뉘어 있습니다. 특정 단계를 수정할 때는 그 단계 폴더의
md 파일만 고치면 됩니다.

**시작점: [docs/00-overview/README.md](docs/00-overview/README.md)** — 원문제 정의, 전체
방향 다이어그램, 진행상황, 유즈케이스가 여기 있습니다.

## 폴더 구조

```
docs/
  00-overview/                 원문제, 전체 다이어그램, 진행상황, 유즈케이스
  01-problem-save/             1단계: 문제 저장 템플릿 (트랙별 + PRD)
  02-problem-analysis/         2단계: 요구사항 분석 방법론(BABOK/EARS/Planguage/Kano/RTM) + 적용 예시
  03-pattern-analysis/         3단계: 패턴/아키텍처 선택 (ADR-0001 완료)
  04-pattern-implementation/   4단계: 패턴 스켈레톤 구현 (진행 예정)
  05-implementation/           5단계: 실제 구현 (미착수)
  06-service/                  6단계: 배포/서비스 (미착수)
  07-maintenance/              7단계: 회고 + 피드백 반영 (미착수)
  catalog/                     패턴 카탈로그, 분석 체크리스트 (공용 참조 자료, 계속 누적)
```
