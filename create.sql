CREATE TABLE Invoice (
	invoice_id bigint NOT NULL PRIMARY KEY,
	net decimal(18, 2),
	gross decimal(18, 2),
	account varchar(20),
)