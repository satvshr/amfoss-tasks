import 'package:flame/components.dart';
import 'package:flame/game.dart';
import 'package:flame/palette.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(GameWidget(game: MyGame()));
}

class MyGame extends FlameGame with HasDraggables {
  late final JoystickComponent joystick;
  @override
  Future<void> onLoad() async {
    final knobPaint = BasicPalette.blue.withAlpha(200).paint();
    final backgroundPaint = BasicPalette.blue.withAlpha(100).paint();
    add(background
      ..sprite = await loadSprite('background.png')
      ..size = size);
    bunny
      ..sprite = await loadSprite('bunny.png')
      ..size = Vector2(100, 100);
    add(bunny);

    joystick = JoystickComponent(
      knob: CircleComponent(radius: 30, paint: knobPaint),
      background: CircleComponent(radius: 50, paint: backgroundPaint),
      margin: const EdgeInsets.only(left: 40, bottom: 40),
    );
    add(joystick);
  }

  SpriteComponent bunny = SpriteComponent();
  SpriteComponent background = SpriteComponent();
  void update(double dt) {
    super.update(dt);
    bunny.position.add(joystick.delta * 3 * dt);
  }
}
