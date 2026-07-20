
from services.guardian.runtime.optimization_bridge import (
    optimize_operation
)


result=optimize_operation({

    "inventory":100,

    "demand":150,

    "capacity":160

})


print(result)
