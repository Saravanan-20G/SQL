select * from suppliers

insert into suppliers(supplier_id,supplier_name,contact_name,phone,email,address) values (1,'san','saran','65978','fbgg@gmail.com','0,sdkoforo')

select * from purchases
select * from projects

select dep_id from dept
where dept_name='bat'

select * from employees

where salary > (select avg(salary) from employees)

select max(salary) from employees where salary < (select max(salary) from employees)

select * from employees order by emp_id desc limit 4