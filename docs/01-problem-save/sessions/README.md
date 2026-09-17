# 세션 (실제로 채운 문제/프로젝트 항목)

이 폴더는 `docs/01-problem-save/`의 템플릿 파일(`algorithm-track.md`, `project-track.md`)을
실제로 채운 결과물이 쌓이는 곳입니다. 템플릿 원본은 건드리지 않고, 여기에 트랙별 하위
폴더를 만들어 항목을 모읍니다.

## 경로 규칙 (4단계에서 확정, `.claude/skills/dev-workflow/SKILL.md` 참고)

```
docs/01-problem-save/sessions/<트랙파일명(확장자 제외)>/<YYYY-MM-DD>-<슬러그>.md
```

예: `docs/01-problem-save/sessions/algorithm-track/2026-09-20-two-sum.md`

트랙파일명은 `docs/01-problem-save/`에 있는 템플릿 파일 이름과 그대로 맞춥니다 —
새 트랙(`README.md`, `prd-template.md`가 아닌 새 `*.md` 파일)을 추가하면 이 폴더에도
같은 이름의 하위 폴더가 자연스럽게 생깁니다.
