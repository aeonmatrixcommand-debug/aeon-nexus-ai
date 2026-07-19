from cloud_runtime.deployment import CloudDeployment
from api_gateway.service import EnterpriseAPI


cloud = CloudDeployment()
api = EnterpriseAPI()


print("=================================")
print(" AEON MATRIX CLOUD PILOT ")
print("=================================")


print("\nCLOUD DEPLOYMENT")
print(cloud.deploy())


print("\nAPI HEALTH")
print(api.health())


print("\nCOMMAND TEST")
print(
    api.execute(
        "OPTIMIZE_WAREHOUSE_OPERATION"
    )
)


print("\n=================================")
print(" AEON MATRIX CUSTOMER PILOT READY ")
print(" Cloud > API > Intelligence > Execution ")
print("=================================")
