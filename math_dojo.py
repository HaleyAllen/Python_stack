
class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, nums):
        self.result = num + nums
        return self
    def subtract(self, num, nums):
        self.result = num - nums
        return self

md = MathDojo()
md.add(2,5).add(5,5).add(6,5)
print(md.result)

md.subtract(4,2).subtract(8,2).subtract(6,4)
print(md.result)



# RESTful ark
# table_name/id/action

# user/new
# user/create
# user/<int:id>
# user/<int:id>/edit
# user/<int:id>/update
# user/<int:id>/delete