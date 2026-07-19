from services.guardian.learning.outcome_collector import (
    OutcomeCollector
)

from services.guardian.learning.learning_engine import (
    LearningEngine
)


collector=OutcomeCollector()

engine=LearningEngine()



def process_outcome(
    trace_id,
    decision,
    result
):

    event=collector.record(

        trace_id,

        decision,

        result,

        True,

        1.0

    )


    learning=engine.analyze(
        collector.history
    )


    return {

        "event":event.to_dict(),

        "learning":learning

    }
