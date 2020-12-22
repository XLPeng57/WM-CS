package gui;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.Panel;
import java.awt.RenderingHints.Key;
import java.awt.font.GlyphVector;
import java.awt.geom.Rectangle2D;

/**
 * Add functionality for double buffering to an AWT Panel class.
 * Used for drawing a maze.
 * 
 * @author Peter Kemper
 *
 */
public class MazePanel extends Panel implements P5Panel {
	private static final long serialVersionUID = 2787329533730973905L;
	/* Panel operates a double buffer see
	 * http://www.codeproject.com/Articles/2136/Double-buffer-in-standard-Java-AWT
	 * for details
	 */
	// bufferImage can only be initialized if the container is displayable,
	// uses a delayed initialization and relies on client class to call initBufferImage()
	// before first use
	private Image bufferImage;  
	public Graphics2D graphics; // obtained from bufferImage, 
	// graphics is stored to allow clients to draw on the same graphics object repeatedly
	// has benefits if color settings should be remembered for subsequent drawing operations
	Color color;
	int rgb;
	static final Color greenWM = Color.decode("#115740");
	final static Color goldWM = Color.decode("#916f41");
	static final Color yellowWM = Color.decode("#FFFF99");
	static final Color CIRCLE_HIGHLIGHT = new Color(1.0f, 1.0f, 1.0f, 0.8f); 
    static final Color CIRCLE_SHADE = new Color(1.0f, 1.0f, 1.0f, 0.3f); //new Color(0.0f, 0.0f, 0.0f, 0.2f); 
    static final Color MAIN_COLOR = greenWM;
    static final Color MARKER_COLOR = Color.black;
    static final Color white = Color.white;
    static final Color gray = Color.gray;
    static final Color red = Color.red;
    static final Color yellow = Color.yellow;
    final private int viewWidth = 400;  // = 400;
	final private int viewHeight = 400; // = 400;
	static Font markerFont = Font.decode("Serif-PLAIN-16");
	/**
	 * Constructor. Object is not focusable.
	 */
	public MazePanel() {
		setFocusable(false);
		bufferImage = null; // bufferImage initialized separately and later
		graphics = null;	// same for graphics
	}
	
	@Override
	public void update(Graphics g) {
		paint(g);
	}
	/**
	 * Method to draw the buffer image on a graphics object that is
	 * obtained from the superclass. 
	 * Warning: do not override getGraphics() or drawing might fail. 
	 */
	public void update() {
		paint(getGraphics());
	}
	
	/**
	 * Draws the buffer image to the given graphics object.
	 * This method is called when this panel should redraw itself.
	 * The given graphics object is the one that actually shows 
	 * on the screen.
	 */
	@Override
	public void paint(Graphics g) {
		if (null == g) {
			System.out.println("MazePanel.paint: no graphics object, skipping drawImage operation");
		}
		else {
			g.drawImage(bufferImage,0,0,null);	
		}
	}

	/**
	 * Obtains a graphics object that can be used for drawing.
	 * This MazePanel object internally stores the graphics object 
	 * and will return the same graphics object over multiple method calls. 
	 * The graphics object acts like a notepad where all clients draw 
	 * on to store their contribution to the overall image that is to be
	 * delivered later.
	 * To make the drawing visible on screen, one needs to trigger 
	 * a call of the paint method, which happens 
	 * when calling the update method. 
	 * @return graphics object to draw on, null if impossible to obtain image
	 */
	public Graphics getBufferGraphics() {
		// if necessary instantiate and store a graphics object for later use
		if (null == graphics) { 
			if (null == bufferImage) {
				bufferImage = createImage(Constants.VIEW_WIDTH, Constants.VIEW_HEIGHT);
				if (null == bufferImage)
				{
					System.out.println("Error: creation of buffered image failed, presumedly container not displayable");
					return null; // still no buffer image, give up
				}		
			}
			graphics = (Graphics2D) bufferImage.getGraphics();
			if (null == graphics) {
				System.out.println("Error: creation of graphics for buffered image failed, presumedly container not displayable");
			}
			else {
				// System.out.println("MazePanel: Using Rendering Hint");
				// For drawing in FirstPersonDrawer, setting rendering hint
				// became necessary when lines of polygons 
				// that were not horizontal or vertical looked ragged
				graphics.setRenderingHint(java.awt.RenderingHints.KEY_ANTIALIASING,
						java.awt.RenderingHints.VALUE_ANTIALIAS_ON);
				graphics.setRenderingHint(java.awt.RenderingHints.KEY_INTERPOLATION,
						java.awt.RenderingHints.VALUE_INTERPOLATION_BILINEAR);
			}
		}
		return graphics;
	}

	@Override
	public void commit() {
		// TODO Auto-generated method stub
		paint(getGraphics());
		
	}

	@Override
	public boolean isOperational() {
		// TODO Auto-generated method stub
		
		if (graphics != null) {
			return true;
		}
		return false;
	}

	@Override
	public void setColor(int rgb) {
		// TODO Auto-generated method stub
		this.rgb = rgb;
		color = new Color(rgb);
		graphics.setColor(color);
	}

	@Override
	public int getColor() {
		// TODO Auto-generated method stub
		
		return color.getRGB();

	}

	@Override
	public int getWallColor(int distance, int cc, int extensionX) {
		// TODO Auto-generated method stub
		final int d = distance / 4;
        // mod used to limit the number of colors to 6
		final int part1 = distance & 7;
        final int add = (extensionX != 0) ? 1 : 0;
        final int rgbValue = ((part1 + 2 + add) * 70) / 8 + 80;
        
        final int RGB_DEF = 20;
        final int RGB_DEF_GREEN = 60;
     
        //System.out.println("Initcolor rgb: " + rgbValue);
        switch (((d >> 3) ^ cc) % 6) {
        case 0:
            color = new Color(rgbValue, RGB_DEF, RGB_DEF);            
            break;
        case 1:
            color = new Color(RGB_DEF, RGB_DEF_GREEN, RGB_DEF);
            break;
        case 2:
            color = new Color(RGB_DEF, RGB_DEF, rgbValue);
            break;
        case 3:
            color = new Color(rgbValue, RGB_DEF_GREEN, RGB_DEF);
            break;
        case 4:
            color = new Color(RGB_DEF, RGB_DEF_GREEN, rgbValue);
            break;
        case 5:
            color = new Color(rgbValue, RGB_DEF, rgbValue);
            break;
        default:
            color = new Color(RGB_DEF, RGB_DEF, RGB_DEF);
            break;
        }
        
        return color.getRGB();
        
	}

	@Override
	public void addBackground(float percentToExit) {
		// TODO Auto-generated method stub
		
		
	    double r = percentToExit * yellowWM.getRed() + (1-percentToExit) * goldWM.getRed();
	    double g = percentToExit * yellowWM.getGreen() + (1-percentToExit) * goldWM.getGreen();
	    double b = percentToExit * yellowWM.getBlue() + (1-percentToExit) * goldWM.getBlue();
	    double a = Math.max(yellowWM.getAlpha(), goldWM.getAlpha());

	    color = new Color((int) r, (int) g, (int) b, (int) a);
		
		graphics.setColor(color);
		graphics.fillRect(0, 0, viewWidth, viewHeight/2);
		// grey rectangle in lower half of screen
		// graphics.setColor(Color.darkGray);
		// dynamic color setting: 
		
		double r1 = percentToExit * Color.lightGray.getRed() + (1-percentToExit) * greenWM.getRed();
	    double g1 = percentToExit * Color.lightGray.getGreen() + (1-percentToExit) * greenWM.getGreen();
	    double b1 = percentToExit * Color.lightGray.getBlue() + (1-percentToExit) * greenWM.getBlue();
	    double a1 = Math.max(Color.lightGray.getAlpha(), greenWM.getAlpha());
		color = new Color((int) r1, (int)g1, (int)b1, (int)a1);
		graphics.setColor(color);
		graphics.fillRect(0, viewHeight/2, viewWidth, viewHeight/2);
	}

	@Override
	public void addFilledRectangle(int x, int y, int width, int height) {
		// TODO Auto-generated method stub
		graphics.fillRect(x, y, width, height);
	}

	@Override
	public void addFilledPolygon(int[] xPoints, int[] yPoints, int nPoints) {
		// TODO Auto-generated method stub
		graphics.fillPolygon(xPoints,yPoints,nPoints);
	}

	@Override
	public void addPolygon(int[] xPoints, int[] yPoints, int nPoints) {
		// TODO Auto-generated method stub
		graphics.drawPolygon(xPoints, yPoints, nPoints);
	}

	@Override
	public void addLine(int startX, int startY, int endX, int endY) {
		// TODO Auto-generated method stub
		graphics.drawLine(startX, startY, endX, endY);
	}

	@Override
	public void addFilledOval(int x, int y, int width, int height) {
		// TODO Auto-generated method stub
		graphics.fillOval(x, y, width, height);
	}

	@Override
	public void addArc(int x, int y, int width, int height, int startAngle, int arcAngle) {
		// TODO Auto-generated method stub
		graphics.drawArc(x, y, width, height, startAngle, arcAngle);
	}

	@Override
	public void addMarker(float x, float y, String str) {
		// TODO Auto-generated method stub
		GlyphVector gv = markerFont.createGlyphVector(graphics.getFontRenderContext(), str);
        Rectangle2D rect = gv.getVisualBounds();
        
        x -= rect.getWidth() / 2;
        y += rect.getHeight() / 2;
        
        graphics.drawGlyphVector(gv, x, y);
	}

	@Override
	public void setRenderingHint(RenderingHints hintKey, RenderingHints hintValue) {
		Key key = null;
		Object value = null;
		// TODO Auto-generated method stub
		
		if (hintKey == RenderingHints.KEY_RENDERING) {
			key = java.awt.RenderingHints.KEY_RENDERING;
		}
		if (hintKey == RenderingHints.KEY_ANTIALIASING) {
			key = java.awt.RenderingHints.KEY_ANTIALIASING;
		}
		if (hintKey == RenderingHints.KEY_INTERPOLATION) {
			key = java.awt.RenderingHints.KEY_INTERPOLATION;
		}
		if (hintValue == RenderingHints.VALUE_RENDER_QUALITY) {
			value = java.awt.RenderingHints.VALUE_RENDER_QUALITY;
		}
		if (hintValue == RenderingHints.VALUE_ANTIALIAS_ON) {
			value = java.awt.RenderingHints.VALUE_ANTIALIAS_ON;
		}
		if (hintValue == RenderingHints.VALUE_INTERPOLATION_BILINEAR) {
			value = java.awt.RenderingHints.VALUE_INTERPOLATION_BILINEAR;
		}
		
		
		graphics.setRenderingHint(key, value);
	}
	
	public void setMarkerFont(String name) {
		
		markerFont = Font.decode(name);
		
		
	}
	
	

}
