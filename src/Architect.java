// The same logic used in the Customer.java & Contractor.java classes also applies to this class !!!!!!
// Including comments
public class Architect {

    String name;
    String phone_num;
    String email;
    String address;

    public Architect(String name, String phone_num, String email, String address) {
        this.name = name;
        this.phone_num = phone_num;
        this.email = email;
        this.address = address;
    }

    public String getName() {
        return name;
    }
    public String getPhone_num() {
        return phone_num;
    }
    public String getEmail() {
        return email;
    }
    public String getAddress() {
        return address;
    }

    public String toString() {
        String output = "";

        output += "\nName            : " + name;
        output += "\nTelephone number: " + phone_num;
        output += "\nEmail address   : " + email;
        output += "\nPhysical address: " + address;

        return output;
    }
}