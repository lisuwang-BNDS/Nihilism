#╔════════════════════════════════════════════════════════════════╗
#║  CYBERPUNK: SAVING HUMANITY - ENHANCED VISUAL DESIGN            ║
#║  Hero: Liv (Neon Pink/Magenta/Purple) - Fills rows              ║
#║  Villain: Lyla (Cyan/Deep Blue/White) - Clears rows             ║
#║  Theme: Free Will vs Genetics | Tech for Good vs Destruction    ║
#╚════════════════════════════════════════════════════════════════╝

import sys
import os
sys.path.append(os.path.dirname(__file__))

from cmu_graphics.cmu_graphics import *
import math
import random

# ═══════════════════════════════════════════════════════════════
# NEW ENHANCED COLOR PALETTE - RICH & VIBRANT
# ═══════════════════════════════════════════════════════════════

# LIV (Hero) - Pink/Magenta/Purple Spectrum
LIV_MAGENTA = rgb(255, 0, 200)      # Main hero color - Vibrant magenta
LIV_PINK = rgb(255, 100, 200)       # Secondary hero - Softer pink
LIV_LIGHT_PINK = rgb(255, 150, 230) # Light accent
LIV_PURPLE = rgb(200, 100, 255)     # Purple blend
LIV_WHITE = rgb(255, 255, 255)      # White highlights

# LYLA (Villain) - Cyan/Blue/Purple Spectrum
LYLA_CYAN = rgb(0, 255, 255)        # Main villain color - Bright cyan
LYLA_DEEP_BLUE = rgb(0, 150, 220)   # Deep blue
LYLA_LIGHT_BLUE = rgb(100, 200, 255)# Light blue
LYLA_BLUE_PURPLE = rgb(100, 150, 255) # Blue-purple blend
LYLA_WHITE = rgb(220, 240, 255)     # Icy white

# Environmental Colors
BG_DARK = rgb(5, 5, 15)             # Ultra dark background
GRID_DARK = rgb(20, 20, 40)         # Grid base color
GRID_LIGHT = rgb(30, 30, 50)        # Alternating grid

# Accents & Highlights
ACCENT_GREEN = rgb(0, 255, 120)     # Bright green
ACCENT_YELLOW = rgb(255, 200, 0)    # Gold yellow
ACCENT_ORANGE = rgb(255, 100, 0)    # Vivid orange
DANGER_RED = rgb(255, 50, 120)      # Danger/glitch color
GLITCH_PURPLE = rgb(200, 0, 200)    # Purple glitch

    
def onAppStart(app):
    app.rows = 16
    app.cols = 10
    app.boardLeft = 70
    app.boardTop = 160
    app.boardWidth = 300
    app.boardHeight = 480
    app.cellBorderWidth = 1
    app.pieceTopRow = None
    app.pieceLeftCol = None
    app.board = [[(None, 0) for _ in range(app.cols)] for _ in range(app.rows)]  # (character, fillLevel)
    
    # Initialize board with population (0-10 fills per cell)
    for row in range(app.rows):
        for col in range(app.cols):
            app.board[row][col] = (None, random.randint(3, 7))  # Random population density
    
    loadTetrisPieces(app)
    app.piece = None
    app.color = None
    app.activeHero = 'liv'  # Start as Liv (can toggle with Tab)
    app.pause = False
    app.stepsPerSecond = 1.5
    app.bestScore = 0
    app.score = 0
    app.population = 80  # Global population percentage
    app.gameover = False
    app.gameOverReason = ""
    app.glitchEffect = False
    app.glitchTimer = 0
    app.backgroundColor = 'white'
    url = 'https://lambda.vgmtreasurechest.com/soundtracks/minecraft/wbslavdc/2-13.%20Aria%20Math.mp3'
    app.sound = Sound(url)
    app.sound.play(loop=True)
    
    loadPiece(app)
    
    
def reset(app):
    old = app.bestScore
    onAppStart(app)
    app.bestScore = old
    

    
    
def onStep(app):
    app.glitchTimer += 1
    if app.glitchTimer > 8:
        app.glitchEffect = False
        app.glitchTimer = 0
    
    if not app.gameover and not app.pause:
        takeStep(app)
    
        
def takeStep(app):
    if not movePiece(app, 1, 0):
        placePieceOnBoard(app)
        processRowsAfterPlacement(app)
        loadPiece(app)
    if app.activeHero == 'liv':
        app.backgroundColor = 'white'
    else:
        app.backgroundColor = 'black'

def processRowsAfterPlacement(app):
    """
    Liv (Hero): Filling rows saves people, but OVER-filling kills them
    Lyla (Villain): Clearing rows kills people
    """
    for row in range(app.rows):
        filledCount = 0
        for col in range(app.cols):
            character, fillLevel = app.board[row][col]
            if character is not None:
                filledCount += 1
        
        # Row is COMPLETELY filled (all 10 cells have pieces)
        if filledCount == app.cols:
            app.glitchEffect = True
            app.glitchTimer = 0
            if app.activeHero == 'liv':
                # LIV LOSES: Over-filled = killed everyone in that row
                app.population -= 15
                app.gameOverReason = "OVER-FILL ERROR: You killed the people you were trying to save!"
            else:
                # LYLA WINS: Successfully cleared the row
                app.population -= 20
                app.score += 150
                app.gameOverReason = "LYLA CLEARED A SECTOR!"
            
            # Remove the row
            app.board.pop(row)
            app.board.insert(0, [(None, random.randint(3, 7)) for _ in range(app.cols)])
        
        # Row is PARTIALLY filled (balance = good for Liv)
        elif filledCount > 0 and filledCount < app.cols:
            if app.activeHero == 'liv':
                # LIV WINS: Partial fill saves some people
                saved = filledCount * 2
                app.population = min(100, app.population + saved // 10)
                app.score += saved
    
    # Check population status
    if app.population <= 0:
        app.bestScore = max(app.score, app.bestScore)
        app.gameover = True
        app.gameOverReason = "POPULATION EXTINCT" if app.activeHero == 'liv' else "LYLA'S VICTORY"
    elif app.population >= 100:
        app.bestScore = max(app.score, app.bestScore)
        app.gameover = True
        app.gameOverReason = "HUMANITY SAVED!"

    
def placePieceOnBoard(app):
    for row in range(len(app.piece)):
        for col in range(len(app.piece[0])):
            if app.piece[row][col]:
                boardRow = row + app.pieceTopRow
                boardCol = col + app.pieceLeftCol
                if 0 <= boardRow < app.rows and 0 <= boardCol < app.cols:
                    _, fillLevel = app.board[boardRow][boardCol]  # FIXED: Extract fillLevel correctly
                    app.board[boardRow][boardCol] = (app.color, fillLevel)
    
    
def redrawAll(app):
    # Vibrant cyberpunk background with gradient effect
    drawRect(0,0, app.width, app.height ,
             fill=app.backgroundColor)
    
    if not app.gameover:
        # Draw top UI panel with gradient vibes
        drawRect(app.width // 2, 75, app.width, 150, fill=GLITCH_PURPLE, opacity=10, border=LIV_MAGENTA, borderWidth=2)
        drawRect(app.width // 2, 75, app.width, 150, fill=LYLA_CYAN, opacity=5, border=LYLA_DEEP_BLUE, borderWidth=1)
        
        # Title with glitch effect - Vibrant magenta
        glitchOffset = random.randint(-2, 2) if app.glitchEffect else 0
        drawLabel('⚡ CYBERPUNK: SAVING HUMANITY ⚡', 
                  app.width // 2 + glitchOffset, 25, 
                  size=24, bold=True, fill=LIV_MAGENTA, font='monospace')
        
        # Hero/Villain display with rich colors
        heroText = f">>> HERO: LIV <<<" if app.activeHero == 'liv' else f">>> VILLAIN: LYLA <<<"
        heroFill = LIV_MAGENTA if app.activeHero == 'liv' else LYLA_CYAN
        drawLabel(heroText, 100, 50, size=14, bold=True, fill=heroFill, font='monospace')
        
        # Mission statement with accent green
        missionText = "FILL ROWS (Don't overfill!)" if app.activeHero == 'liv' else "CLEAR SECTORS (Destroy all!)"
        drawLabel(missionText, 100, 70, size=10, fill=ACCENT_GREEN, font='monospace')
        
        # Stats with dual colors
        drawLabel(f'SCORE: {app.score:05d}', 320, 50, size=11, bold=True, fill=ACCENT_YELLOW, font='monospace')
        drawLabel(f'BEST: {app.bestScore:05d}', 320, 70, size=11, bold=True, fill=LYLA_LIGHT_BLUE, font='monospace')
        
        # Population bar (critical metric)
        drawPopulationBar(app)
        
        # Main game board with enhanced borders
        drawBoardBorder(app)
        drawBoard(app)
        drawPiece(app)
        
        # Controls panel with orange accent
        drawLabel('[P] PAUSE | [TAB] SWITCH | [SPACE] DROP | [S/C] ROTATE', 
                  app.width // 2, app.height - 30, size=8, fill=ACCENT_ORANGE, font='monospace')
        
    else:
        # Game over screen with dynamic glitch effects
        drawRect(app.width // 2, app.height // 2, app.width, app.height, 
                 fill=BG_DARK, opacity=95)
        
        # Multiple glitch border layers for intense effect
        for i in range(4):
            offset = random.randint(-3, 3)
            glitchColor = [DANGER_RED, GLITCH_PURPLE, LYLA_CYAN, LIV_MAGENTA][i % 4]
            drawRect(app.width // 2 + offset, app.height // 2 + random.randint(-2, 2), 450, 500, 
                    fill=None, border=glitchColor, borderWidth=2, opacity=20)
        
        # Game over message - Red danger
        drawLabel('▓ GAME OVER ▓', app.width // 2, app.height // 2 - 80, 
                 size=48, bold=True, fill=DANGER_RED, font='monospace')
        
        # Reason with appropriate color
        reasonColor = LIV_MAGENTA if 'HUMANITY' in app.gameOverReason else LYLA_CYAN
        drawLabel(app.gameOverReason, app.width // 2, app.height // 2 - 20,
                 size=16, bold=True, fill=reasonColor, font='monospace')
        
        # Final stats - Gold yellow
        drawLabel(f'FINAL SCORE: {app.score}', app.width // 2, app.height // 2 + 20,
                 size=13, fill=ACCENT_YELLOW, font='monospace')
        drawLabel(f'BEST SCORE: {app.bestScore}', app.width // 2, app.height // 2 + 45,
                 size=13, fill=ACCENT_YELLOW, font='monospace')
        
        # Restart instruction with vibrant color
        drawLabel('[R] RESTART | [TAB] SWITCH HERO', app.width // 2, app.height // 2 + 100,
                 size=12, bold=True, fill=ACCENT_GREEN, font='monospace')

def drawPopulationBar(app):
    """Draw population health bar with rich gradients"""
    barLeft = app.boardLeft
    barTop = 130
    barWidth = 300
    barHeight = 15
    
    # Background bar with gradient effect
    drawRect(barLeft + barWidth // 2, barTop, barWidth, barHeight, 
            fill=GRID_DARK, border=LYLA_LIGHT_BLUE, borderWidth=2)
    
    # Population fill with dynamic colors
    fillWidth = (app.population / 100) * barWidth
    if app.population > 70:
        fillColor = ACCENT_GREEN  # Healthy
    elif app.population > 40:
        fillColor = ACCENT_YELLOW  # Caution
    else:
        fillColor = DANGER_RED  # Critical
    
    if fillWidth > 0:
        drawRect(barLeft + fillWidth // 2, barTop, fillWidth, barHeight, 
                fill=fillColor, opacity=85)
        # Glow effect
        drawRect(barLeft + fillWidth // 2, barTop, fillWidth, barHeight, 
                fill=fillColor, opacity=25)
    
    # Label with magenta/cyan
    labelColor = LIV_MAGENTA if app.activeHero == 'liv' else LYLA_CYAN
    drawLabel(f'█ POPULATION: {int(app.population)}% █', 
             barLeft - 20, barTop, size=9, bold=True, fill=labelColor, font='monospace')

def drawBoard(app):
    for row in range(app.rows):
        for col in range(app.cols):
            character, fillLevel = app.board[row][col]
            drawCell(app, row, col, character, fillLevel)

def drawBoardBorder(app):
    # Triple-layer neon border for intense cyberpunk look
    # Outer magenta border (Liv's color)
    drawRect(app.boardLeft, app.boardTop, app.boardWidth, app.boardHeight,
             fill=None, border=LIV_MAGENTA, borderWidth=3)
    # Middle cyan border (Lyla's color)
    drawRect(app.boardLeft, app.boardTop, app.boardWidth, app.boardHeight,
             fill=None, border=LYLA_CYAN, borderWidth=1, opacity=60)
    # Inner green accent
    drawRect(app.boardLeft, app.boardTop, app.boardWidth, app.boardHeight,
             fill=None, border=ACCENT_GREEN, borderWidth=1, opacity=30)
           
def onKeyPress(app, key):
    if not app.gameover:
        if '0' <= key <= '6':
            loadPiece(app, int(key))
        elif key == 'left':
            movePiece(app, 0, -1)
        elif key == 'right':
            movePiece(app, 0, 1)
        elif key == 's':
            rotatePieceClockwise(app)
        elif key == 'c':
            rotatePieceCounterClockwise(app)
        elif key == 'up':
            movePiece(app, -1, 0)
        elif key == 'down':
            movePiece(app, 1, 0)
        elif key == 'space':
            hardDropPiece(app)
        elif key == 'p':
            app.pause = not app.pause
        elif key == 'tab':
            # Switch between Liv and Lyla
            app.activeHero = 'lyla' if app.activeHero == 'liv' else 'liv'
            loadPiece(app)
    
    if key == 'r':
        reset(app)
    elif key == 'tab' and app.gameover:
        app.activeHero = 'lyla' if app.activeHero == 'liv' else 'liv'
        reset(app)
            
        
def rotatePieceClockwise(app):
    oldRows, oldCols = len(app.piece), len(app.piece[0])
    newRows, newCols = oldCols, oldRows
    oldPiece = app.piece
    oldTopRow = app.pieceTopRow
    oldLeftCol = app.pieceLeftCol
    app.piece = rotate2dListClockwise(app.piece)
    centerRow = oldTopRow + oldRows // 2
    centerCol = oldLeftCol + oldCols // 2
    app.pieceTopRow = centerRow - newRows // 2
    app.pieceLeftCol = centerCol - newCols // 2
    Right = app.pieceLeftCol + newCols 
    Down = app.pieceTopRow + newRows 
    if not(pieceIsLegal(app, app.pieceLeftCol, Right, app.pieceTopRow, Down)):
        app.pieceTopRow = oldTopRow
        app.pieceLeftCol = oldLeftCol
        app.piece = oldPiece 
        
        
def rotatePieceCounterClockwise(app):
    oldRows, oldCols = len(app.piece), len(app.piece[0])
    newRows, newCols = oldCols, oldRows
    oldPiece = app.piece
    oldTopRow = app.pieceTopRow
    oldLeftCol = app.pieceLeftCol
    app.piece = rotate2dListCounterClockwise(app.piece)
    centerRow = oldTopRow + oldRows // 2
    centerCol = oldLeftCol + oldCols // 2
    app.pieceTopRow = centerRow - newRows // 2
    app.pieceLeftCol = centerCol - newCols // 2
    Right = app.pieceLeftCol + newCols 
    Down = app.pieceTopRow + newRows 
    if not(pieceIsLegal(app, app.pieceLeftCol, Right, app.pieceTopRow, Down)):
        app.pieceTopRow = oldTopRow
        app.pieceLeftCol = oldLeftCol
        app.piece = oldPiece 
        

        
def hardDropPiece(app):
    while movePiece(app, 1, 0):
        pass
        
        
def movePiece(app, dr, dc):
    Left = app.pieceLeftCol + dc
    Right = Left + len(app.piece[0]) - 1
    Up = app.pieceTopRow + dr
    Down = Up + len(app.piece) - 1
    if (pieceIsLegal(app, Left, Right, Up, Down)): 
        app.pieceTopRow += dr
        app.pieceLeftCol += dc
        return True
    return False
        
def pieceIsLegal(app, L, r, u, d):
    if (L < 0 or r >= app.cols or u < 0 or d >= app.rows):
        return False
    
    for row in range(u, d + 1):
        for col in range(L, r + 1):
            character, _ = app.board[row][col]
            if character is not None and app.piece[row - u][col - L]:
                return False
    return True

def loadPiece(app, pieceIndex=None):
    if pieceIndex is None:
        pieceIndex = random.randrange(len(app.tetrisPieces))
    app.piece = app.tetrisPieces[pieceIndex]
    
    # Assign color based on active hero - Use new rich colors
    if app.activeHero == 'liv':
        app.color = LIV_MAGENTA  # Updated to vibrant magenta
    else:
        app.color = LYLA_CYAN  # Updated to bright cyan
    
    app.pieceTopRow = 0
    app.pieceLeftCol = math.floor(((app.cols - len(app.piece[0])) * 0.5))
    if not (pieceIsLegal(app, app.pieceLeftCol, app.pieceLeftCol + len(app.piece[0]) - 1, 
                         app.pieceTopRow, app.pieceTopRow + len(app.piece) - 1)):
        app.bestScore = max(app.score, app.bestScore)
        app.gameover = True
        app.gameOverReason = f"BOARD OVERFLOW - {app.activeHero.upper()}'S END"


def drawPiece(app):
    if app.pieceTopRow != None and app.pieceLeftCol != None:
        rows, cols = len(app.piece), len(app.piece[0])
        for row in range(rows):
            for col in range(cols):
                if app.piece[row][col]:
                    drawCell(app, row + app.pieceTopRow, col + app.pieceLeftCol, app.color, 10)

def drawCell(app, row, col, character, fillLevel):
    """Draw cyberpunk-styled cell with rich colors and effects"""
    cellLeft, cellTop = getCellLeftTop(app, row, col)
    cellWidth, cellHeight = getCellSize(app)
    
    # Alternating grid background with richer colors
    baseColor = GRID_DARK if (row + col) % 2 == 0 else GRID_LIGHT
    drawRect(cellLeft + cellWidth // 2, cellTop + cellHeight // 2, cellWidth - 2, cellHeight - 2,
             fill=baseColor, border=LYLA_LIGHT_BLUE, borderWidth=1, opacity=40)
    
    # If character is present (filled by piece)
    if character is not None:
        # Determine rich color gradient based on hero
        if character == LIV_MAGENTA:  # Liv's piece
            barColor = LIV_MAGENTA
            accentColor = LIV_LIGHT_PINK
            glowColor = LIV_PURPLE
        else:  # Lyla's piece
            barColor = LYLA_CYAN
            accentColor = LYLA_LIGHT_BLUE
            glowColor = LYLA_BLUE_PURPLE
        
        # Fill indicator (how full the cell is)
        fillRatio = fillLevel / 10
        fillHeight = (cellHeight - 4) * fillRatio
        
        # Main fill bar
        drawRect(cellLeft + cellWidth // 2, cellTop + cellHeight - fillHeight // 2 - 2, 
                cellWidth - 4, fillHeight, fill=barColor, opacity=90)
        
        # Accent layer for depth
        drawRect(cellLeft + cellWidth // 2, cellTop + cellHeight - fillHeight // 2 - 2, 
                cellWidth - 4, fillHeight * 0.5, fill=accentColor, opacity=50)
        
        # Glow effect
        drawRect(cellLeft + cellWidth // 2, cellTop + cellHeight - fillHeight // 2 - 2, 
                cellWidth - 4, fillHeight, fill=glowColor, opacity=15)
        
        # Bright border highlight for energy effect
        drawRect(cellLeft + cellWidth // 2, cellTop + cellHeight // 2, cellWidth - 2, cellHeight - 2,
                fill=None, border=accentColor, borderWidth=1, opacity=70)

def getCellLeftTop(app, row, col):
    cellWidth, cellHeight = getCellSize(app)
    cellLeft = app.boardLeft + col * cellWidth
    cellTop = app.boardTop + row * cellHeight
    return (cellLeft, cellTop)

def getCellSize(app):
    cellWidth = app.boardWidth / app.cols
    cellHeight = app.boardHeight / app.rows
    return (cellWidth, cellHeight)
    
def rotate2dListClockwise(L):
    oldRows, oldCols = len(L), len(L[0])
    newRows, newCols = oldCols, oldRows
    M = [[None] * newCols for r in range(newRows)]
    for oldRow in range(oldRows):
        for oldCol in range(oldCols):
            M[oldCol][oldRows - 1 - oldRow] = L[oldRow][oldCol]
    return M
    
def rotate2dListCounterClockwise(L):
    oldRows, oldCols = len(L), len(L[0])
    newRows, newCols = oldCols, oldRows
    M = [[None] * newCols for r in range(newRows)]
    for oldRow in range(oldRows):
        for oldCol in range(oldCols):
            M[oldCols - 1 - oldCol][oldRow] = L[oldRow][oldCol]
    return M

def loadTetrisPieces(app):
    """Load standard Tetris pieces"""
    iPiece = [[True,  True,  True,  True]]
    jPiece = [[True,  False, False],
              [True,  True,  True]]
    lPiece = [[False, False, True],
              [True,  True,  True]]
    oPiece = [[True,  True],
              [True,  True]]
    sPiece = [[False, True,  True],
              [True,  True,  False]]
    tPiece = [[False, True,  False],
              [True,  True,  True]]
    zPiece = [[True,  True,  False],
              [False, True,  True]]
    
    app.tetrisPieces = [iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece]
                              
                              
def main():
    runApp(width=420, height=700)

main()