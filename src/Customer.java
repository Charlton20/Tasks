// Create a class for the customer
public class Customer {
    // Below are the attributes for this class
    String name;
    String phone_num;
    String email;
    String address;

    // Create a method for the above attributes
    public Customer(String name, String phone_num, String email, String address) {
        this.name = name;
        this.phone_num = phone_num;
        this.email = email;
        this.address = address;
    }

    // Call the above method using setters and getters
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

    // Use a toString to print out the informatio
    public String toString() {
        String output = "";

        output += "\nName            : " + name;
        output += "\nTelephone number: " + phone_num;
        output += "\nEmail address   : " + email;
        output += "\nPhysical address: " + address;

        return output;
    }
}
