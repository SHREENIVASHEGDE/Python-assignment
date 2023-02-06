-- create
CREATE TABLE company(
  comp_nm TEXT ,
  comp_id integer primary key,
  open float(3),
  high float(3),
  low float(3),
  close float(3),
  adjclse float(3),
  volume integer
);

-- insert
INSERT INTO company VALUES ('IBM', 0001, 127.09, 127.09, 126.07, 188.99, 187.99, 34548000);
INSERT INTO company VALUES ('INFOSYS', 0002, 1576, 1576, 1561, 1578.45, 1568.56, 58769800);
INSERT INTO company VALUES ('CISCO', 0003, 89.08, 98.08, 88.77, 89.09, 90.88, 23458900);
INSERT INTO company VALUES ('SONY', 0004, 128.8, 183, 180.9, 179.09, 130.09, 32458000);
INSERT INTO company VALUES ('WIPRO',0005, 1456, 1678, 1456, 1456.7, 1456, 58798000);

-- fetch 
SELECT * FROM company;

--adding new column
alter table company 
add revenue text;

--display
select * from company;

--insert/update data 
update company
set revenue = '16 B', close = '180' where comp_id = 0001;

--display table
select * FROM company;





