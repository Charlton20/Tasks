/*
Import java.util.*
Ask the user what they would like to do and provide them with an option (y/n)
If the user selects y for yes, the program should call the specific function for that selection otherwise, print goodbye
 */
import java.util.*;

public class Main {
    public static void main(String[] args) {
        System.out.print("Would you like to add a new project?\n\nEnter y/n: ");
        Scanner input0 = new Scanner(System.in);
        String add_proj = input0.next();

        if (add_proj.equals("y")) {

            project_add();
        }
        else if (add_proj.equals("n")) {
            System.out.println("Goodbye ;)");
        }
    }
    //Create a function called project_add that adds a new project
    private static void project_add() {
        String project_name;
        String project_num;
        String building_type;
        String address;
        String erf_number;
        double amount;
        double paid;
        String due_date;

        // Request for a project name from the user
        Scanner input1 = new Scanner(System.in);
        System.out.println("Enter project name: ");
        project_name = input1.next();
        System.out.println(project_name);

        // Request for a project umber from the user
        Scanner input2 = new Scanner(System.in);
        System.out.println("Enter project number: ");
        project_num = input2.next();
        System.out.println(project_num);

        // Request for the type of building from the user
        Scanner input3 = new Scanner(System.in);
        System.out.println("Enter type of building: ");
        building_type = input3.next();
        System.out.println(building_type);

        // Request for the address from the user
        Scanner input4 = new Scanner(System.in);
        System.out.println("Enter address: ");
        address = input4.next();
        System.out.println(address);

        // Request for the erf number from the user
        Scanner input5 = new Scanner(System.in);
        System.out.println("Enter erf_number number: ");
        erf_number = input5.next();
        System.out.println(erf_number);

        // Request for the total amount from the user
        Scanner input6 = new Scanner(System.in);
        System.out.println("Enter total amount: ");
        amount = input6.nextDouble();
        System.out.println("R" + amount);

        // Request for the total amount paid from the user
        Scanner input7 = new Scanner(System.in);
        System.out.println("Enter total amount paid: ");
        paid = input7.nextDouble();
        System.out.println("R" + paid);

        // Request for the project deadline from the user
        Scanner input8 = new Scanner(System.in);
        System.out.println("Enter project due date: ");
        due_date = input8.next();
        System.out.println(due_date);

        // Print out all the information entered by user above
        System.out.println("\n***********************************************");
        System.out.println("Details:");
        System.out.println("***********************************************\n");
        System.out.println("Project name           : " + project_name);
        System.out.println("Project number         : " + project_num);
        System.out.println("Building type          : " + building_type);
        System.out.println("Physical address       : " + address);
        System.out.println("Erf number             : " + erf_number);
        System.out.println("Total amount           : R" + amount);
        System.out.println("Amount of paid to date : R" + paid);
        System.out.println("Project due date       : " + due_date);
        System.out.println("\n***********************************************");


        // The below code if for the class Customer.java
        Customer customerA = new Customer("Sasha Dys", "+27 21 706 2549", "sash@gmail.com", "8, 6th Av, Constantia");

        // Print the details above in an easy-to-read format
        System.out.println("Customer:\n***********************************************");
        System.out.println(customerA + "\n\n***********************************************");


        // The below code is for the class Architect.java
        Architect architectA = new Architect("Jeff Adams", "+27 83 705 3648", "jeff@gmail.com", "5, 2nd Road, Salt River");

        // Print the details above in an easy-to-read format
        System.out.println("Architect:\n***********************************************");
        System.out.println(architectA + "\n\n***********************************************");


        // The below code is for the class Contractor.java
        Contractor contractorA = new Contractor("David Sams", "+27 74 332 2549", "david@gmail.com", "16, Jeff-coat St, Bergvliet");

        // Print the details above in an easy-to-read format
        System.out.println("Contractor:\n***********************************************");
        System.out.println(contractorA + "\n***********************************************\n");


//----------------------------------------------------------------------------------------------------------------------
        // Now the program should provide the user with another option to change amount paid
        System.out.println("would you like to update total amount paid?\ny/n: ");
        Scanner input9 = new Scanner(System.in);
        String quest_update_fee = input9.next();

        // If the user selects y for yes, the program should call the fee_update function
        if (quest_update_fee.equals("y")) {
            paid = amount_update();
        }
        else if (quest_update_fee.equals("n")) {
            System.out.println("Goodbye ;)");
        }

        System.out.println("\nTotal amount updated!");
        System.out.println("***********************************************");
        System.out.println("Project name        :" + project_name);
        System.out.println("Project number      : " + project_num);
        System.out.println("Building type       : " + building_type);
        System.out.println("Physical address    : " + address);
        System.out.println("Erf number          : " + erf_number);
        System.out.println("Total amount        : R" + amount);
        System.out.println("Amount paid to date : R" + paid);
        System.out.println("Project due date    : " + due_date);
        System.out.println("***********************************************");


//----------------------------------------------------------------------------------------------------------------------
        // Now the program should provide the user with another option to change the due date
        System.out.println("\nwould you like to update the due date?\ny/n: ");
        Scanner input10 = new Scanner(System.in);
        String quest_update_date = input10.next();

        // If the user selects y for yes, the program should call the fee_update function
        if (quest_update_date.equals("y")) {
            due_date = due_date_update();
        }
        else if (quest_update_date.equals("n")) {
            System.out.println("Goodbye ;)");
        }

        System.out.println("\nDue date updated!");
        System.out.println("***********************************************");
        System.out.println("Project name        :" + project_name);
        System.out.println("Project number      : " + project_num);
        System.out.println("Building type       : " + building_type);
        System.out.println("Physical address    : " + address);
        System.out.println("Erf number          : " + erf_number);
        System.out.println("Total amount        : R" + amount);
        System.out.println("Amount paid to date : R" + paid);
        System.out.println("Project due date    : " + due_date);
        System.out.println("***********************************************");


//----------------------------------------------------------------------------------------------------------------------
        // Now the program should provide the user with another option to change the contractors details
        System.out.println("\nwould you like to change the contractors contact details?\ny/n: ");
        Scanner input11 = new Scanner(System.in);
        String quest_update_details = input11.next();

        // If the user selects y for yes, the program should call the contractor_update function
        if (quest_update_details.equals("y")) {
             contractor_update();
            System.out.println("Phone number updated!!");

        }
        else if (quest_update_details.equals("n")) {
            System.out.println("Goodbye ;)");

//----------------------------------------------------------------------------------------------------------------------
        }
    }

    // Create a function that updates the total amount paid
    private static double amount_update() {
        double paid;
        System.out.println("Enter total amount paid to date: ");
        Scanner input9 = new Scanner(System.in);
        paid = input9.nextDouble();
        return paid;
    }

    //Create a function that updates the due date of the project
    private static String due_date_update() {
        String due_date;
        System.out.println("Enter new due date: ");
        Scanner input10 = new Scanner(System.in);
        due_date = input10.next();
        return due_date;
    }

    // Create a function that updates the contractors details
    private static void contractor_update() {
        System.out.println("Enter new phone number: ");
        Scanner input11 = new Scanner(System.in);
        String phone_num = input11.next();
    }

}
