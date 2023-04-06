from entities.container import Container

con = Container()

numbers = (1, 2, 3, 4, 5)

con.add("1")

print(con.list())

con.add(*numbers)

print(con.list())