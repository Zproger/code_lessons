from pprint import pprint


user = {"results":[{"gender":"male","name":{"title":"Mr","first":"Justin","last":"Olivier"},"location":{"street":{"number":523,"name":"Quai Charles-De-Gaulle"},"city":"Paris","state":"Drôme","country":"France","postcode":51764,"coordinates":{"latitude":"-19.2225","longitude":"-68.3569"},"timezone":{"offset":"+2:00","description":"Kaliningrad, South Africa"}},"email":"justin.olivier@example.com","login":{"uuid":"6c804a47-4d9b-4ba1-89dd-804afd34436a","username":"smallsnake602","password":"michael","salt":"s1MRUMfb","md5":"d85994ea97ea7de241ea0cf749d702bd","sha1":"6511dbe3abe9295746b555ee02cc40e4379ab8d6","sha256":"ad5acbdaad6d96ed09ea14a56803b102e7b9948211c88a6d7cf2f5c44f1074e4"},"dob":{"date":"1948-01-24T00:48:29.473Z","age":75},"registered":{"date":"2007-09-02T17:56:14.623Z","age":15},"phone":"05-82-23-23-60","cell":"06-44-98-98-83","id":{"name":"INSEE","value":"1480011382632 50"},"picture":{"large":"https://randomuser.me/api/portraits/men/67.jpg","medium":"https://randomuser.me/api/portraits/med/men/67.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/67.jpg"},"nat":"FR"}],"info":{"seed":"7dd14e900358b41f","results":1,"page":1,"version":"1.4"}}

print(user)
pprint(user)


