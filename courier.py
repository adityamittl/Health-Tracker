from trycourier import Courier

client = Courier(auth_token="pk_prod_N2TAPNS8VZ4HFSQS4W49Q6NT8MTC")

resp = client.send(
  event="personalized-welcome-email",
  recipient="c9f20127-0563-4a5e-aeb9-eef6175bb4af",
  profile={
  },
  data={
    'firstname': "Aditya",
  },
)