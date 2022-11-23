public class Person
{
    private String vorname;
    private String nachname;
    
    public Person(String vorname, String nachname)
    {
        this.vorname = vorname;
        this.nachname = nachname;
    }
    
    public String getName()
    {
        return vorname + " " + nachname;
    }
}