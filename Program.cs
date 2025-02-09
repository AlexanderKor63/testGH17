using Microsoft.Data.SqlClient;
// comment
String conStr="Server=(local)\\SQLExpress;Initial Catalog=AdventureWorks;User Id=sa;Password=1234;TrustServerCertificate=true";

var con = new SqlConnection(conStr);
con.Open();


var cmd = new SqlCommand("select top 5 FirstName from Person.Contact", con);
var reader=cmd.ExecuteReader();
while(reader.Read()) Console.WriteLine("Name:{0}",reader[0]);

con.Close();
