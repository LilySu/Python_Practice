
Delete Duplicate Rows

delete * from table
group by columns
having count(*) > 1

Extract Names That Start With

select employee_name
from employees
where employee_name LIKE 'A%' OR employee_name LIKE 'B%'
order by employee_name