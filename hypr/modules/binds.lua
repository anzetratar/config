local mainMod = "SUPER"

-- Applications
hl.bind(mainMod .. " + Return", hl.dsp.exec_cmd("foot"))

hl.bind(mainMod .. " + D", hl.dsp.exec_cmd("rofi -show drun"))
hl.bind(mainMod .. " + F", hl.dsp.exec_cmd("dolphin"))

-- Window
hl.bind(mainMod .. " + BackSpace", hl.dsp.window.close())
hl.bind(mainMod .. " + T", hl.dsp.window.float({ action = "toggle" }))
hl.bind(mainMod .. " + N", hl.dsp.exec_cmd("pgrep -x hyprsunset >/dev/null && pkill -x hyprsunset || hyprsunset -t 4000"))

-- Mouse
hl.bind(mainMod .. " + mouse:272", hl.dsp.window.drag(), { mouse = true })    -- ALT + LMB: Move a window
hl.bind(mainMod .. " + mouse:273", hl.dsp.window.resize(), { mouse = true })  -- ALT + RMB: Resize a window

-- Focus
hl.bind(mainMod .. " + Left", hl.dsp.focus({ direction = "left" }))
hl.bind(mainMod .. " + Right", hl.dsp.focus({ direction = "right" }))
hl.bind(mainMod .. " + Up", hl.dsp.focus({ direction = "up" }))
hl.bind(mainMod .. " + Down", hl.dsp.focus({ direction = "down" }))

-- Workspaces
for i = 1, 9 do
    hl.bind(mainMod .. " + " .. i, hl.dsp.focus({ workspace = i }))
    hl.bind(mainMod .. " + SHIFT + " .. i, hl.dsp.window.move({ workspace = i }))
end

-- Swap windows
hl.bind(mainMod .. " + SHIFT + Left", hl.dsp.window.swap({ direction = "left" }))
hl.bind(mainMod .. " + SHIFT + Right", hl.dsp.window.swap({ direction = "right" }))
hl.bind(mainMod .. " + SHIFT + Up", hl.dsp.window.swap({ direction = "up" }))
hl.bind(mainMod .. " + SHIFT + Down", hl.dsp.window.swap({ direction = "down" }))

--Keyboard
hl.bind(mainMod .. " + SPACE", hl.dsp.exec_cmd("hyprctl switchxkblayout all next"))
