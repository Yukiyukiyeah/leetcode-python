select max(Salary)
as SecondHighestSalary
from Employee
where Salary not in (select max(Salary) from Employee)

select(
  select distinct Salary
  from Employee
  order by Salary desc
  limit 1 offset 1
)as SecondHighestSalary

/* limit n子句表示查询结果返回前n条数据

offset n表示跳过x条语句 */