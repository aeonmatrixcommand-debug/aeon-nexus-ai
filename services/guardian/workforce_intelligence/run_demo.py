<<<<<<< HEAD
from .skills.skill_analyzer import analyze_skill
from .coach.work_coach import AIWorkCoach
from .learning.learning_path import create_learning_path
from .signals.adoption_signal import create_adoption_signal
=======
>>>>>>> origin/main


employee = {
    "ai_usage": 30
}


skill = analyze_skill(employee)

coach = AIWorkCoach()


analysis = coach.analyze({
    "skill_gap": skill
})

learning = create_learning_path(skill)

signal = create_adoption_signal(70)


print({
    "skill_analysis": "COMPLETED",
    "coach_analysis": "COMPLETED",
    "learning_path": "GENERATED",
    "adoption_signal": "RECORDED"
})
