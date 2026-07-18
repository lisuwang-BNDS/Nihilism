# ⚡ CYBERPUNK: SAVING HUMANITY ⚡

## Game Overview

A revolutionary cyberpunk-themed Tetris variant where **free will battles genetic destiny**. Two heroes, two opposing philosophies, one population to save (or destroy).

---

## 🎮 Characters & Themes

### **LIV** - The Hero (Neon Pink | RGB 255,185,244)
- **Philosophy**: Free Will & Tech for Good
- **Goal**: FILL ROWS (but not completely!)
- **Objective**: Save humanity by selectively filling population sectors
- **Challenge**: Over-filling a row = population death. Strategic partial fills are the key!
- **Mechanics**: 
  - Partial fills (1-9 cells) = Saves lives & earns points
  - Complete fill (all 10 cells) = GAME OVER (overfill catastrophe)

### **LYLA** - The Villain (Cyan Neon | RGB 179,233,255)
- **Philosophy**: Genetic Determinism & Epigenetic Control
- **Goal**: CLEAR ROWS (Destroy all people)
- **Objective**: Extinguish humanity through systematic sector clearing
- **Challenge**: Race against time to clear sectors faster than Liv can defend
- **Mechanics**:
  - Each cleared row = Population damage
  - Victory = Entire population extinction

---

## 🎮 Gameplay Mechanics

### Core Gameplay Loop
1. **Pieces Fall**: Colored Tetris blocks descend (Liv's pink or Lyla's cyan)
2. **Place Strategically**: 
   - **As LIV**: Fill rows partially to save populations
   - **As LYLA**: Clear entire rows to destroy populations
3. **Population Meter**: Central health bar showing humanity survival %
4. **Dynamic Scoring**: Points awarded for strategic plays

### Row Processing Rules
- **Partial Fill (1-9 cells)**: Liv saves those people (+points, +population)
- **Complete Fill (10 cells)**: 
  - **If Liv**: Over-filled! Population dies (-15%, -game over message)
  - **If Lyla**: Cleared sector! Population dies (-20%, +150 points)
- **Population Depletion**: ≤0% = Lyla's victory / Population extinct
- **Population Recovery**: ≥100% = Humanity saved! (Liv wins)

---

## 🕹️ Controls

| Key | Action |
|-----|--------|
| **← / →** | Move piece left/right |
| **↑** | Soft rotate clockwise |
| **↓** | Soft drop piece |
| **SPACE** | Hard drop (instant placement) |
| **S** | Rotate clockwise |
| **C** | Rotate counter-clockwise |
| **P** | Pause/Resume |
| **TAB** | Switch between Liv & Lyla |
| **R** | Restart game |

---

## 🎨 Visual Design (Cyberpunk Aesthetic)

### Color Palette
- **Liv (Hero)**: Neon Pink (RGB 255,185,244) + White
- **Lyla (Villain)**: Cyan Neon (RGB 179,233,255) + Black
- **Accents**: Neon Purple (RGB 200,100,255), Neon Green (RGB 0,255,150)
- **Danger**: Glitch Red (RGB 255,50,100)
- **Background**: Dark Cyberpunk (RGB 15,15,30)

### UI Elements
- **Neon Borders**: Double-layer glowing effect on game board
- **Glitch Effects**: Game over screen has animated glitch borders
- **Population Bar**: Color-coded health meter (green→purple→red)
- **Monospace Font**: Cyberpunk terminal aesthetic
- **Character Displays**: Live hero/villain status with mission statements

---

## 📊 Scoring System

### LIV (Hero) - Population Saver
- **Partial Fill**: `fillCount × 2` points per filled cell
- **Full Overfill**: Immediate game over (-15% population)
- **Population Recovery**: +saved people % on strategic fills

### LYLA (Villain) - Population Destroyer  
- **Cleared Sector**: 150 points base
- **Row Clear Multiplier**: Further clears increase damage
- **Population Loss**: -20% per cleared sector

### Global Metrics
- **Best Score**: Persistent across games
- **Population %**: 0-100 scale, affects game ending
- **Round Score**: Current game points

---

## 🏆 Winning Conditions

### LIV Wins
- **Population reaches 100%**: Humanity saved!
- **Successfully defend against Lyla's attempts**

### LYLA Wins
- **Population reaches 0%**: Extinction achieved!
- **Successfully clear sectors faster than Liv defends**

### Game Over Scenarios
1. `OVER-FILL ERROR`: Liv completely filled a row (Liv active)
2. `LYLA CLEARED A SECTOR`: Villain cleared a row (Lyla active)
3. `POPULATION EXTINCT`: Reached 0% (Lyla victory)
4. `HUMANITY SAVED`: Reached 100% (Liv victory)
5. `BOARD OVERFLOW`: Piece couldn't fit at spawn (Either character)

---

## 🎮 Strategy Tips

### Playing as LIV
- ✓ Don't fill rows completely - strategic partial fills are your strength
- ✓ Leave gaps to prevent accidental overfills
- ✓ Prioritize saving heavily populated rows (high fill levels)
- ✓ Use population bar as your main objective metric
- ✗ Avoid complete fills at all costs

### Playing as LYLA
- ✓ Focus on clearing entire rows for maximum damage
- ✓ Use rotation strategically to complete rows faster
- ✓ Hard-drop pieces to speed up your assault
- ✓ Target sectors approaching full capacity
- ✗ Partial fills are wasted moves

---

## 🔧 Technical Features

### Implemented in Custom Python Tetris Engine
- **Board**: 16 rows × 10 columns with population tracking
- **Pieces**: All 7 standard Tetris tetrominoes
- **Physics**: Real-time gravity, collision detection
- **UI**: CMU Graphics library with custom cyberpunk theme
- **Performance**: 1.5 steps/second gameplay speed

### Enhanced Features Over Original
1. ✨ **Cyberpunk Visual Theme**: Complete redesign with neon colors
2. 👥 **Dual Characters**: Switch between hero/villain with Tab key
3. 📊 **Population System**: Dynamic health bar replacing score
4. 🎯 **Strategic Mechanics**: Partial vs complete fills matter
5. 🎪 **Glitch Effects**: Visual feedback for major events
6. 🎨 **Professional UI**: Organized panels, clear information hierarchy
7. ⌨️ **Enhanced Controls**: Better rotation, hard drop, character switching

---

## 🚀 How to Play

1. **Run the game**: `python Te.py`
2. **Choose your hero**: Press TAB to switch (start as Liv)
3. **Play your strategy**:
   - As **Liv**: Place pieces to partially fill rows
   - As **Lyla**: Complete entire rows
4. **Watch population meter**: Your score depends on it!
5. **Press TAB mid-game** to see Lyla's perspective
6. **Press R to restart** with your best score preserved
7. **Press P to pause** if you need a break

---

## 📝 Game Philosophy

This game represents the eternal struggle between:
- **Liv's Vision**: Individual agency, technology as liberation, strategic adaptation
- **Lyla's Vision**: Deterministic systems, genetic inevitability, systematic control

Neither path is predetermined. Victory belongs to the player who best understands their character's strengths and plays with intention.

**Will you save humanity with Liv's adaptive strategies, or will you assert Lyla's systematic dominance?**

---

**Created**: 2024 Cyberpunk Game Jam
**Theme**: Free Will vs Fate | Tech for Good vs Tech for Control
**Status**: Ready for play! 🎮⚡
