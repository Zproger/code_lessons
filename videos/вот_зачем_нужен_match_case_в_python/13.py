
banned_list = ["user1", "user2"]
value = ["user3", "pass3"]

match value:
    case user, password if user is not banned_list:
        print(f"Открыт доступ. ({user=}, {password=})")

