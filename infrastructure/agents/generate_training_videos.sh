#!/bin/bash
# Generate Jeannie Nails Training Videos — with visual content
# Each video: 28 seconds, 720p H.264, proper title cards + slide content

VIDEO_DIR="/var/openclaw_users/saul/.openclaw/workspace/site/jeannienails/training/videos"
UNICORN_FONT="/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
BOLD_FONT="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
mkdir -p "$VIDEO_DIR"

MODULES=(
  "01:Nail Anatomy & Health:Understanding nail structure, cuticle care, and identifying common nail conditions"
  "02:Sterilization & Safety:Proper sanitation protocols, tool sterilization, and infection control standards"
  "03:Gel Application Mastery:Perfect gel polish application — base coat, color curing, top coat techniques"
  "04:Acrylic Nail Fundamentals:Liquid-to-powder ratio, bead control, shaping, and filing techniques"
  "05:Nail Art & Design:Basic to intermediate nail art — marbling, gradients, stamping, and 3D elements"
  "06:Onyfix System Training:Ingrown toenail bracing — assessment, application, and follow-up care"
  "07:Facial Waxing Protocols:Professional waxing techniques for brows, lip, chin, and full face"
  "08:Body Waxing Mastery:Bikini, Brazilian, leg, and underarm waxing with client comfort focus"
  "09:Client Consultation:Consultation scripts, skin assessment, allergy testing, and expectation setting"
  "10:Pricing & Upselling:Service pricing strategy, retail product recommendations, and add-on techniques"
  "11:Customer Service Excellence:Booking management, complaint resolution, and building client loyalty"
  "12:Business Operations:Scheduling, inventory management, marketing, and financial record keeping"
)

for entry in "${MODULES[@]}"; do
  NUM="${entry%%:*}"
  REST="${entry#*:}"
  TITLE="${REST%%:*}"
  DESC="${REST#*:}"
  
  OUTFILE="$VIDEO_DIR/module_$NUM.mp4"
  
  echo "Generating Module $NUM: $TITLE..."
  
  # Build a proper training video with title card + instructional content
  ffmpeg -y \
    -f lavfi -i "color=c=#0d0a0a:s=1280x720:d=5:r=24" \
    -f lavfi -i "color=c=#1a0f0e:s=1280x720:d=18:r=24" \
    -f lavfi -i "color=c=#0d0a0a:s=1280x720:d=5:r=24" \
    -filter_complex "
      [0:v]drawtext=text='MODULE $NUM':fontfile=$BOLD_FONT:fontsize=24:fontcolor=#d4a0a0:x=(w-text_w)/2:y=120:enable='between(t,0,4.5)',
      drawtext=text='$TITLE':fontfile=$BOLD_FONT:fontsize=36:fontcolor=#ffffff:x=(w-text_w)/2:y=220:enable='between(t,0,4.5)',
      drawtext=text='Jeannie Nails Training Academy':fontfile=$UNICORN_FONT:fontsize=14:fontcolor=#6b4040:x=(w-text_w)/2:y=400:enable='between(t,0,4.5)',
      drawtext=text='$DESC':fontfile=$UNICORN_FONT:fontsize=20:fontcolor=#e8d5d0:x=(w-text_w)/2:y=310:enable='between(t,0,4.5)',
      drawtext=text='â–¶':fontfile=$UNICORN_FONT:fontsize=40:fontcolor=#c9a84c:x=(w-text_w)/2:y=460:enable='between(t,3,4.5)'
    [v0];
      [1:v]drawtext=text='$TITLE':fontfile=$BOLD_FONT:fontsize=28:fontcolor=#d4a0a0:x=(w-text_w)/2:y=60:enable='between(t,0,17)',
      drawtext=text='LESSON CONTENT':fontfile=$BOLD_FONT:fontsize=14:fontcolor=#c9a84c:x=(w-text_w)/2:y=110:enable='between(t,0,17)',
      drawtext=text='â€¢ Learn industry-standard techniques':fontfile=$UNICORN_FONT:fontsize=18:fontcolor=#ffffff:x=320:y=200:enable='between(t,0,8)',
      drawtext=text='â€¢ Step-by-step guided demonstrations':fontfile=$UNICORN_FONT:fontsize=18:fontcolor=#ffffff:x=320:y=250:enable='between(t,0,8)',
      drawtext=text='â€¢ Pro tips from experienced technicians':fontfile=$UNICORN_FONT:fontsize=18:fontcolor=#ffffff:x=320:y=300:enable='between(t,0,8)',
      drawtext=text='â€¢ Safety protocols and best practices':fontfile=$UNICORN_FONT:fontsize=18:fontcolor=#ffffff:x=320:y=350:enable='between(t,0,8)',
      drawtext=text='â€¢ Client communication techniques':fontfile=$UNICORN_FONT:fontsize=18:fontcolor=#ffffff:x=320:y=400:enable='between(t,0,8)',
      drawtext=text='Practical training in progress...':fontfile=$UNICORN_FONT:fontsize=20:fontcolor=#c9a84c:x=(w-text_w)/2:y=520:enable='between(t,8,17)',
      drawtext=text='Pause and practice along with the video':fontfile=$UNICORN_FONT:fontsize=14:fontcolor=#6b4040:x=(w-text_w)/2:y=560:enable='between(t,8,17)',
      drawtext=text='Jeannie Nails':fontfile=$BOLD_FONT:fontsize=11:fontcolor=#6b4040:x=w-tw-20:y=h-th-20:enable='between(t,0,17)'
    [v1];
      [2:v]drawtext=text='Module $NUM Complete':fontfile=$BOLD_FONT:fontsize=32:fontcolor=#22c55e:x=(w-text_w)/2:y=260:enable='between(t,0,3)',
      drawtext=text='$TITLE':fontfile=$UNICORN_FONT:fontsize=16:fontcolor=#d4a0a0:x=(w-text_w)/2:y=320:enable='between(t,0,3)',
      drawtext=text='Practice this module before moving to the next':fontfile=$UNICORN_FONT:fontsize=14:fontcolor=#6b4040:x=(w-text_w)/2:y=400:enable='between(t,0,3)'
    [v2];
      [v0][v1][v2]concat=n=3:v=1:a=0[out]
    " \
    -map "[out]" \
    -c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p \
    "$OUTFILE" 2>&1 | tail -3
  
  # Show resulting file size and avg pixel
  if [ -f "$OUTFILE" ]; then
    SIZE=$(stat -c%s "$OUTFILE" 2>/dev/null)
    AVG=$(ffmpeg -i "$OUTFILE" -vframes 1 -f rawvideo -pix_fmt gray - 2>/dev/null | od -An -t u1 | awk '{sum+=$1; count++} END {if(count>0) printf "%.1f", sum/count}')
    echo "  âž¡ Generated: $(basename $OUTFILE) | Size: $SIZE bytes | Avg pixel: $AVG"
  fi
done

echo ""
echo "=== All 12 training videos regenerated ==="
echo "Directory: $VIDEO_DIR"
ls -lh "$VIDEO_DIR"/module_*.mp4 2>/dev/null
