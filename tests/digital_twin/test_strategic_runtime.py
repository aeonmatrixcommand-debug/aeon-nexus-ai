from digital_twin.strategic.strategic_runtime import StrategicRuntime


def test_strategic_runtime():

    result = StrategicRuntime().execute(
        [
            {
                "type":"cost_risk",
                "impact":
                "transportation_cost_increase"
            }
        ]
    )


    assert (
        result["decision"]["decision"]
        ==
        "optimize_logistics"
    )


    assert (
        result["simulation"]
        ["cost_reduction"]
        > 0
    )
