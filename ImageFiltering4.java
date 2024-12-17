import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

import javax.imageio.ImageIO;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;

public class ImageFiltering4 {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        System.out.println("enter the file location / path : ");
        String filePath = input.nextLine();
        System.out.println("1.convert image to grayscale\n2.Converted to Pseudocolor");
        System.out.println("enter the option:");
        int option = input.nextInt();
        File file = new File(filePath);
        BufferedImage img = null;

        try {
            img = ImageIO.read(file);
        } catch (IOException e) {
            System.out.println("Error occurred while loading the image");
            e.printStackTrace();
            return;
        }

        if (img != null) {
            img = resizeImage(img, 500, 500); 

            switch (option) {
                case 1:
                    img = convertToGrayscale(img);
                    System.out.println("Converted to Grayscale");
                    break;
                case 2:
                    img = convertToPseudocolor(img);
                    System.out.println("Converted to Pseudocolor");
                    break;
                default:
                    System.out.println("Invalid option selected.");
                    return;
            }

            display(img);
        }
    }

    public static BufferedImage resizeImage(BufferedImage originalImage, int width, int height) {
        BufferedImage resizedImage = new BufferedImage(width, height, originalImage.getType());
        Graphics2D g2d = resizedImage.createGraphics();
        g2d.drawImage(originalImage, 0, 0, width, height, null);
        g2d.dispose();
        return resizedImage;
    }

    public static BufferedImage convertToGrayscale(BufferedImage img) {
        int width = img.getWidth();
        int height = img.getHeight();

        BufferedImage grayscale = new BufferedImage(width, height, BufferedImage.TYPE_BYTE_GRAY);
        Graphics2D g2d = grayscale.createGraphics();
        g2d.drawImage(img, 0, 0, null);
        g2d.dispose();

        return grayscale;
    }

    public static BufferedImage convertToPseudocolor(BufferedImage img) {
        int width = img.getWidth();
        int height = img.getHeight();

        BufferedImage pseudocolorImage = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);

        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
         
                int pixel = img.getRGB(x, y);

                int red = (pixel >> 16) & 0xff;
                int green = (pixel >> 8) & 0xff;
                int blue = pixel & 0xff;

                int intensity = (red + green + blue) / 3;

                int newRed = 0, newGreen = 0, newBlue = 0;

                if (intensity < 85) { 
                    newBlue = 255;
                    newGreen = intensity * 3;
                } else if (intensity < 170) { 
                    newGreen = 255;
                    newRed = (intensity - 85) * 3;
                } else { 
                    newRed = 255;
                    newBlue = (intensity - 170) * 3;
                }

                int newPixel = (newRed << 16) | (newGreen << 8) | newBlue;

                
                pseudocolorImage.setRGB(x, y, newPixel);
            }
        }

        return pseudocolorImage;
    }

    public static void display(BufferedImage img) {
        JFrame frame = new JFrame("Image Display");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(img.getWidth(), img.getHeight());

        JLabel label = new JLabel(new ImageIcon(img));
        frame.add(label);

        frame.pack();
        frame.setVisible(true);
    }
}
