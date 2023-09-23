import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import math

x = [5, 7, 9]
y = [0.56, 11.74, 30.13]
errors = [0.08, 1.08, 1.5]

dataotherx = [7,9,10.2]
dataothery = [12.7,25.9,56.96]
dataothererror = [1.44,3.16,2.28]


outx = [10.2]
outy = [21.38]
outerror = [1.10]

#conx = [3.75, 7.5, 10,12.5,17.5,3, 5]
#cony = [3.6114,42.5124,85.4712,132.9382,256.6849,1.45, 11.9]
#conerror = [0.4562,1.2123,3.705,15.7362,19.5461,0.05, 0.5]
conx = [3.75, 7.5,10,3, 5]
cony = [3.6114,42.5124,85.4712,1.45, 11.9]
conerror = [0.4562,1.2123,3.705,0.05, 0.5]

#condx = [3, 5]
#condy = [1.45, 11.9]
#conderror = [0.05, 0.5]


plt.errorbar(conx, cony, yerr=conerror, marker='o', linestyle='', color='black',
             markersize=6, capsize=5, elinewidth=1, label='APS/TEMED')
concoefficients = np.polyfit(conx, cony, 2)
consmooth_x = np.linspace(min(conx), max(conx), 100)

# Evaluate the polynomial using the coefficients and smooth x values
consmooth_y = np.polyval(concoefficients, consmooth_x)
# Plot the original data and the fitted curve
plt.plot(consmooth_x, consmooth_y, color='black', alpha=0.2)
cona, conb, conc = concoefficients


# Print the polynomial equation
print(f"APS/TEMED's Polynomial equation: {cona:.4f}x^2 + {conb:.4f}x + {conc:.4f}")
# Create the scatter plot with error bars
plt.errorbar(x, y, yerr=errors, marker='o', linestyle='', color='#3949ab',
             markersize=6, capsize=5, elinewidth=1,  label='LAP August')

coefficients = np.polyfit(x, y, 2)
smooth_x = np.linspace(min(x), max(x), 100)

# Evaluate the polynomial using the coefficients and smooth x values
smooth_y = np.polyval(coefficients, smooth_x)
# Plot the original data and the fitted curve
plt.plot(smooth_x, smooth_y, color='#3949ab', alpha=0.2)
a, b, c = coefficients

# Print the polynomial equation
print(f"LAP's Polynomial equation: {a:.4f}x^2 + {b:.4f}x + {c:.4f}")

#plt.errorbar(condx, condy, yerr=conderror, marker='o', linestyle='', color='purple',
             #markersize=6, capsize=5, elinewidth=1, label='APS/TEMED Dixon')
#condcoefficients = np.polyfit(condx, condy, 2)
#condsmooth_x = np.linspace(min(condx), max(condx), 100)

# Evaluate the polynomial using the coefficients and smooth x values
#condsmooth_y = np.polyval(condcoefficients, condsmooth_x)
# Plot the original data and the fitted curve
#plt.plot(condsmooth_x, condsmooth_y, color='purple', alpha=0.6)
#conda, condb, condc = condcoefficients

# Print the polynomial equation
#print(f"APS/TEMED's Dixon Polynomial equation: {conda:.4f}x^2 + {condb:.4f}x + {condc:.4f}")

plt.errorbar(dataotherx, dataothery, yerr=dataothererror, marker='o', linestyle='', color='purple',
             markersize=6, capsize=5, elinewidth=1,  label='LAP September')

plt.errorbar(outx, outy, yerr=outerror, marker='o', linestyle='', color='red',
             markersize=6, capsize=5, elinewidth=1,  label='LAP outlier(s)')


# Enable minor ticks on the y-axis
plt.minorticks_on()

# Customize the minor tick appearance (e.g., every 5 units)
plt.gca().yaxis.set_minor_locator(MultipleLocator(2))
plt.gca().xaxis.set_minor_locator(MultipleLocator(1))


#plt.axhline(y=10, color='red', linestyle='--', alpha = 0.3)

# Add labels and a legend
plt.xlabel('Monomer wt %')
plt.ylabel('E* (kPa)')
plt.title('Hertz Model Data Analysis')
plt.legend()



def LAPequation(x):
    return a*x**2+b*x+c
def APSequation(conx):
    return cona*conx**2+conb*conx+conc

first = input("Do you want to do something?")
if first == "yes":

    ask = input("Do want to get an equivalent elastic modulus?")
    while ask == "yes":
        stringElastic = input("What value elastic modulus do you want?")
        elastic = float(stringElastic)
        plt.axhline(y=elastic, color='red', linestyle='--', alpha=0.3)


        LAPc = c - elastic  # Move the constant to the other side
        APSc = conc - elastic
        # Calculate the discriminant (the value inside the square root)
        discriminant = b ** 2 - 4 * a * LAPc
        # Check if the discriminant is non-negative
        if discriminant >= 0:
            # Calculate the two solutions
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
            print(f"Solutions for LAP: x1 = {x1} wt%, x2 = {x2} wt%")
        else:
            print("No real solutions for LAP. Discriminant is negative.")
        discriminant = conb ** 2 - 4 * cona * APSc
        # Check if the discriminant is non-negative
        if discriminant >= 0:
            # Calculate the two solutions
            x1 = (-conb + math.sqrt(discriminant)) / (2 * cona)
            x2 = (-conb - math.sqrt(discriminant)) / (2 * cona)
            print(f"Solutions for APS/TEMED: x1 = {x1} wt%, x2 = {x2} wt%")
        else:
            print("No real solutions for APS/TEMED. Discriminant is negative.")
        ask = input("Do want to get an equivalent elastic modulus?")


    ask2 = input("Do you want to compare a specfic wt% of APS/TEMED gel?")
    while ask2== "yes":
        stringwtAPS = input("What value wt% of APS/TEMED do you want to compare?")
        wtAPS = float(stringwtAPS)
        elasticwtAPS = APSequation(wtAPS)
        plt.axhline(y=elasticwtAPS, color='green', linestyle='--', alpha=0.3)

        LAPc = c - elasticwtAPS  # Move the constant to the other side
        APSc = conc - elasticwtAPS
        # Calculate the discriminant (the value inside the square root)
        discriminant = b ** 2 - 4 * a * LAPc
        # Check if the discriminant is non-negative
        if discriminant >= 0:
            # Calculate the two solutions
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
            print(f"Solutions for LAP: x1 = {x1} wt%, x2 = {x2} wt%")
        else:
            print("No real solutions for LAP. Discriminant is negative.")
        discriminant = conb ** 2 - 4 * cona * APSc
        # Check if the discriminant is non-negative
        if discriminant >= 0:
            # Calculate the two solutions
            x1 = (-conb + math.sqrt(discriminant)) / (2 * cona)
            x2 = (-conb - math.sqrt(discriminant)) / (2 * cona)
            print(f"Solutions for APS/TEMED: x1 = {x1} wt%, x2 = {x2} wt%")
        else:
            print("No real solutions for APS/TEMED. Discriminant is negative.")
        ask2 = input("Do you want to compare a specfic wt% of APS/TEMED gel?")

    ask3 = input("Do you want to compare a specfic wt% of LAP gel?")
    while ask3== "yes":
        stringwtLAP = input("What value wt% of LAP do you want to compare?")
        wtLAP = float(stringwtLAP)
        elasticwtLAP = LAPequation(wtLAP)
        plt.axhline(y=elasticwtLAP, color='purple', linestyle='--', alpha=0.3)

        LAPc = c - elasticwtLAP  # Move the constant to the other side
        APSc = conc - elasticwtLAP
        # Calculate the discriminant (the value inside the square root)
        discriminant = b ** 2 - 4 * a * LAPc
        # Check if the discriminant is non-negative
        if discriminant >= 0:
            # Calculate the two solutions
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
            print(f"Solutions for LAP: x1 = {x1} wt%, x2 = {x2} wt%")
        else:
            print("No real solutions for LAP. Discriminant is negative.")
        discriminant = conb ** 2 - 4 * cona * APSc
        # Check if the discriminant is non-negative
        if discriminant >= 0:
            # Calculate the two solutions
            x1 = (-conb + math.sqrt(discriminant)) / (2 * cona)
            x2 = (-conb - math.sqrt(discriminant)) / (2 * cona)
            print(f"Solutions for APS/TEMED: x1 = {x1} wt%, x2 = {x2} wt%")
        else:
            print("No real solutions for APS/TEMED. Discriminant is negative.")
        ask3 = input("Do you want to compare a specfic wt% of LAP gel?")
    save = input("Do you want to save plot?")
    if save == "yes":
        file = input("file name: ")
        aspect_ratio = 16 / 9
        fig = plt.gcf()
        fig.set_size_inches(fig.get_size_inches() * aspect_ratio)
        plt.savefig(file, dpi=300)
        plt.show()
    else:
        plt.show()
else:
    plt.show()



